from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.functional import cached_property
from gallery import settings
from pathlib import Path
from datetime import datetime
import os


class Image(models.Model):

    data = models.FileField(upload_to='images')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def get_extension(self):
        data, extension = os.path.splitext(self.data.name)
        return extension

    @cached_property
    def slug(self):
        return slugify(self.title)

    @property
    def title(self):
        if hasattr(self, '_title'):
            return self._title
        """ Derive a title from the original filename """
        # remove extension
        filename = Path(self.data.name).with_suffix('').name
        # convert spacing characters to whitespaces
        name = filename.translate(str.maketrans('_', ' '))
        # return with first letter caps
        return name.title()

    # Temporary override for album highlights
    @title.setter
    def title(self, name):
        self._title = name

    def get_absolute_url(self):
        return reverse('gallery:image_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=250)
    images = models.ManyToManyField(Image, blank=True, related_name='image_albums')
    highlight = models.OneToOneField(Image,
                                     related_name='album_highlight',
                                     null=True, blank=True,
                                     on_delete=models.SET_NULL
                                     )

    @property
    def slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('gallery:album_detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        return self.title

    def get_extension(self):
        images, extension = os.path.splitext(self.images.name)
        return extension
