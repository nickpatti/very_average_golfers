from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, FormView, CreateView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin
from gallery.models import Image, Album
from gallery.forms import ImageCreateForm, ImageCommentForm
from comments.models import ImageComments
from gallery import settings
from stylechange.models import ColourScheme, Template
from django.db.models import Count
from blog.models import Post


class GallerySettingsMixin(object):
    """ Apply Gallery's Settings to a view """

    def get_context_data(self, **kwargs):
        """ Make settings available the template """
        context = super(GallerySettingsMixin, self).get_context_data(**kwargs)
        context['logo_path'] = settings.GALLERY_LOGO_PATH
        context['gallery_title'] = settings.GALLERY_TITLE
        context['hdpi_factor'] = settings.GALLERY_HDPI_FACTOR
        context['image_margin'] = settings.GALLERY_IMAGE_MARGIN
        context['footer_info'] = settings.GALLERY_FOOTER_INFO
        context['footer_email'] = settings.GALLERY_FOOTER_EMAIL
        context['colourscheme'] = ColourScheme.objects.all()[0]
        context['templates'] = Template.objects.all()
        context['homepage'] = Post.objects.all()
        # context['num_post'] = ImageComments.objects.filter(post_id=id).count()
        return context


class ImageView(GallerySettingsMixin, DetailView, FormMixin):
    model = Image
    form_class = ImageCommentForm

    def get_context_data(self, **kwargs):
        context = super(ImageView, self).get_context_data(**kwargs)
        context['album_images'] = []
        context['apk'] = self.kwargs.get('apk')
        context['form'] = ImageCommentForm(initial={'image': self.object})

        if context['apk']:
            context['album'] = Album.objects.get(pk=context['apk'])
            images = context['album'].images.all()
            album_images = sorted(images, key=lambda i: i.pk)
            context['album_images'] = album_images
            context['next_image'] = None
            context['previous_image'] = None
            for i in range(len(album_images)):
                if self.object.pk == album_images[i].pk:
                    if i > 0:
                        context['previous_image'] = album_images[i - 1]
                    if i < len(album_images) - 1:
                        context['next_image'] = album_images[i + 1]

        return context

    def get_success_url(self, **kwargs):
        return reverse('gallery:image_detail', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs.get('pk')
        form.save()
        return super(ImageView, self).form_valid(form)


class ImageList(GallerySettingsMixin, ListView):
    model = Image

    def get_queryset(self):
        # Order by newest first
        return super(ImageList, self).get_queryset().order_by('-pk')


class ImageCreate(GallerySettingsMixin, LoginRequiredMixin, FormView):
    """ Embedded drag and drop image upload"""
    login_url = '/admin/login/'
    form_class = ImageCreateForm
    template_name = 'gallery/image_upload.html'

    def form_valid(self, form):
        """ Bulk create images based on form data """
        image_data = form.files.getlist('data')
        for data in image_data:
            image = Image.objects.create(data=data)
            image.image_albums.add(form.data['apk'])
        messages.success(self.request, "Images added successfully")
        return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        return_url = reverse('gallery:image_list')
        if next_url:
            return_url = next_url
        return return_url

    def form_invalid(self, form):
        response = super().form_invalid(form)
        next_url = self.request.POST.get('next')
        if next_url:
            # TODO: Preserve error message
            return redirect(next_url)
        else:
            return response


class AlbumView(GallerySettingsMixin, DetailView):
    model = Album

    def get_context_data(self, **kwargs):
        context = super(AlbumView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        album = super(AlbumView, self).get_queryset()
        return album

    def get_context_data(self, **kwargs):
        context = super(AlbumView, self).get_context_data(**kwargs)
        images = context['album'].images.all()
        context['images'] = sorted(images, key=lambda i: i.pk)
        # context['num_post'] = ImageComments.objects.filter(images).count()
        return context


class AlbumList(GallerySettingsMixin, ListView):
    model = Album
    template_name = 'gallery/album_list.html'

    def get_queryset(self):
        # Return a list of albums containing a highlight even if none is selected
        album_list = []
        for album in super(AlbumList, self).get_queryset().order_by('-pk'):
            # if there is no highlight but there are images in the album, use the first
            if not album.highlight and album.images.count():
                first_image = album.images.earliest('id')
                album.highlight = first_image
            album_list.append(album)
            if album.highlight:
                album.highlight.title = album.title  # override highlight title
        return album_list


class AlbumCreate(GallerySettingsMixin, CreateView):
    model = Album
    template_name = 'gallery/album_create.html'
    fields = ['title']
