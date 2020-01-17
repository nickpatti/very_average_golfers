from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Post, CompetitionsPost, TrophyPost, SocialsPost, TraditionsPost, LinksPost, YearRoll, EventRoll, Members, AllTimeRoll
from stylechange.models import ColourScheme, Template
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class ColourView(object):
    def get_context_data(self, **kwargs):
        context = super(ColourView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        context['templates'] = Template.objects.all()
        context['homepage'] = Post.objects.all()
        return context


def home(request):
    context = {
        'posts': Post.objects.all(),
        'colourscheme': ColourScheme.objects.all()[0]
    }
    return render(request, 'blog/home.html', context)


class PostListView(ColourView, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        context['template'] = Template.objects.all()[0]
        return context


class PostDetailView(ColourView, DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class PostCreateView(ColourView, LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'logo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class PostUpdateView(ColourView, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'logo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class PostDeleteView(ColourView, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(PostDeleteView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context

#################### MEMBERS IN OFFICE ###############################


class MembersListView(ColourView, ListView):
    model = Members
    template_name = 'members/members.html'
    context_object_name = 'member'


class MembersDetailView(ColourView, DetailView):
    model = Members
    template_name = 'members/members_detail.html'


class MembersUpdateView(ColourView, UpdateView):
    model = Members
    template_name = 'members/members_update.html'
    fields = ['title', 'high_chair', 'high_chair_image', 'chair', 'chair_image', 'under_chair', 'under_chair_image', 'humble', 'humble_image']


def summary(request):
    context = {
        'colourscheme': ColourScheme.objects.all()[0]
    }
    return render(request, 'members/summary_responsibility.html', context)

####################ARTICLES OF ASSOCIATION VIEW ######################


class ArticlesListView(ColourView, ListView):
    model = TrophyPost
    template_name = 'articles/articles.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super(ArticlesListView, self).get_context_data(**kwargs)
        context['competitions'] = CompetitionsPost.objects.all().order_by('priority')
        context['socials'] = SocialsPost.objects.all().order_by('priority')
        context['traditions'] = TraditionsPost.objects.all().order_by('priority')
        return context


class TrophyListView(ColourView, ListView):
    model = TrophyPost
    template_name = 'articles/trophy.html'
    context_object_name = 'trophy'
    ordering = ['date_posted']

    def get_context_data(self, **kwargs):
        context = super(TrophyListView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class TrophyDetailView(ColourView, DetailView):
    model = TrophyPost
    template_name = 'articles/trophy_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TrophyDetailView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class TrophyCreateView(ColourView, LoginRequiredMixin, CreateView):
    model = TrophyPost
    fields = ['title', 'content']
    template_name = 'articles/trophy_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TrophyCreateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class TrophyUpdateView(ColourView, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TrophyPost
    fields = ['title', 'content']
    template_name = 'articles/trophy_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(TrophyUpdateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class TrophyDeleteView(ColourView, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TrophyPost
    success_url = '/articles'
    template_name = 'articles/trophy_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(TrophyDeleteView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


def competitions(request):
    context = {
        'competitions': CompetitionsPost.objects.all()
    }
    return render(request, 'articles/competitions_main.html', context)


class CompetitionListView(ColourView, ListView):
    model = CompetitionsPost
    template_name = 'articles/competition_main.html'
    context_object_name = 'competitions'
    ordering = ['priority']

    def get_context_data(self, **kwargs):
        context = super(CompetitionListView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class CompetitionDetailView(ColourView, DetailView):
    model = CompetitionsPost
    template_name = 'articles/competition_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CompetitionDetailView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class CompetitionCreateView(ColourView, LoginRequiredMixin, CreateView):
    model = CompetitionsPost
    fields = ['title', 'content' 'content2', 'priority']
    template_name = 'articles/competition_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CompetitionCreateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class CompetitionUpdateView(ColourView, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CompetitionsPost
    fields = ['title', 'content', 'content2', 'priority']
    template_name = 'articles/competition_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(CompetitionUpdateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class CompetitionDeleteView(ColourView, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CompetitionsPost
    success_url = '/articles'
    template_name = 'articles/competitions_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(CompetitionDeleteView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context

########        SOCIALS            ########


def socials(request):
    context = {
        'socials': SocialsPost.objects.all()
    }
    return render(request, 'articles/socials.html', context)


class SocialListView(ColourView, ListView):
    model = SocialsPost
    template_name = 'articles/socials.html'
    context_object_name = 'socials'
    ordering = ['priority']

    def get_context_data(self, **kwargs):
        context = super(SocialListView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class SocialDetailView(ColourView, DetailView):
    model = SocialsPost
    template_name = 'articles/socials_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SocialDetailView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class SocialCreateView(ColourView, LoginRequiredMixin, CreateView):
    model = SocialsPost
    fields = ['title', 'content', 'content2', 'priority']
    template_name = 'articles/socials_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SocialCreateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class SocialUpdateView(ColourView, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SocialsPost
    fields = ['title', 'content', 'content2', 'priority']
    template_name = 'articles/socials_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(SocialUpdateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class SocialDeleteView(ColourView, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = SocialsPost
    success_url = '/articles'
    template_name = 'articles/socials_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(SocialDeleteView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


def traditions(request):
    context = {
        'traditions': TraditionsPost.objects.all()
    }
    return render(request, 'articles/traditions.html', context)


class TraditionListView(ColourView, ListView):
    model = TraditionsPost
    template_name = 'articles/traditions.html'
    context_object_name = 'traditions'
    ordering = ['priority']

    def get_context_data(self, **kwargs):
        context = super(TraditionListView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class TraditionDetailView(ColourView, DetailView):
    model = TraditionsPost
    template_name = 'articles/traditions_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TraditionDetailView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class TraditionCreateView(ColourView, LoginRequiredMixin, CreateView):
    model = TraditionsPost
    fields = ['title', 'content', 'content2', 'priority']
    template_name = 'articles/traditions_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TraditionCreateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class TraditionUpdateView(ColourView, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TraditionsPost
    fields = ['title', 'content', 'content2', 'priority']
    template_name = 'articles/traditions_create_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(TraditionUpdateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class TraditionDeleteView(ColourView, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TraditionsPost
    success_url = '/articles'
    template_name = 'articles/traditions_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(TraditionDeleteView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context

################# ROLL OF HONOUR TEMPORARY #######################


class RollListView(ColourView, ListView):
    model = YearRoll
    template_name = 'roll_honour/roll_honour.html'
    context_object_name = 'rolls'
    ordering = ['-title']

    def get_context_data(self, **kwargs):
        context = super(RollListView, self).get_context_data(**kwargs)
        context['events'] = EventRoll.objects.all()
        context['records'] = AllTimeRoll.objects.all()
        context['traditions'] = TraditionsPost.objects.all()
        return context


class RollYearListView(ColourView, ListView):
    model = YearRoll
    template_name = 'roll_honour/roll_honour_year.html'
    context_object_name = 'years'
    ordering = ['-title']


class RollYearDetailView(ColourView, DetailView):
    model = YearRoll
    template_name = 'roll_honour/year_detail.html'


class RollYearCreateView(ColourView, CreateView):
    model = YearRoll
    template_name = 'roll_honour/year_create.html'
    fields = ['title', 'table']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RollYearUpdateView(ColourView, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = YearRoll
    template_name = 'roll_honour/year_create.html'
    fields = ['title', 'table']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class RollYearDeleteView(ColourView, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = YearRoll
    success_url = '/'
    template_name = 'roll_honour/year_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class RollEventListView(ColourView, ListView):
    model = EventRoll
    template_name = 'roll_honour/roll_honour_event.html'
    context_object_name = 'events'
    ordering = ['priority']


class RollEventDetailView(ColourView, DetailView):
    model = EventRoll
    template_name = 'roll_honour/event_detail.html'


class RollEventCreateView(ColourView, CreateView):
    model = EventRoll
    template_name = 'roll_honour/event_create.html'
    fields = ['title', 'table']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RollEventUpdateView(ColourView, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EventRoll
    template_name = 'roll_honour/event_create.html'
    fields = ['title', 'table']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class RollEventDeleteView(ColourView, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EventRoll
    success_url = '/'
    template_name = 'roll_honour/event_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AllTimeListView(ColourView, ListView):
    model = AllTimeRoll
    template_name = 'roll_honour/alltime_roll.html'
    context_object_name = 'alltime'
    ordering = ['priority']


class AllTimeDetailView(ColourView, DetailView):
    model = AllTimeRoll
    template_name = 'roll_honour/alltime_detail.html'


class AllTimeCreateView(ColourView, CreateView):
    model = AllTimeRoll
    template_name = 'roll_honour/alltime_create.html'
    fields = ['title', 'table']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AllTimeUpdateView(ColourView, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AllTimeRoll
    template_name = 'roll_honour/alltime_create.html'
    fields = ['title', 'table']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AllTimeDeleteView(ColourView, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AllTimeRoll
    success_url = '/'
    template_name = 'roll_honour/event_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

############################ Links ###############################


def links(request):
    context = {
        'links': LinksPost.objects.all()
    }
    return render(request, 'links/links.html', context)


class LinksPostListView(ColourView, ListView):
    model = LinksPost
    template_name = 'links/links.html'
    context_object_name = 'links'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super(LinksPostListView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class LinksPostDetailView(ColourView, DetailView):
    model = LinksPost
    template_name = 'links/links_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LinksPostDetailView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class LinksPostCreateView(ColourView, LoginRequiredMixin, CreateView):
    model = LinksPost
    fields = ['title', 'image']
    template_name = 'links/links_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LinksPostCreateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class LinksPostUpdateView(ColourView, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = LinksPost
    fields = ['title', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(LinksPostUpdateView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context


class LinksPostDeleteView(ColourView, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = LinksPost
    success_url = '/'
    template_name = 'links/links_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(LinksPostDeleteView, self).get_context_data(**kwargs)
        context['colourscheme'] = ColourScheme.objects.all()[0]
        return context
