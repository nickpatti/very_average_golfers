from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ChangeLog
from blog.views import ColourView


class ChangeLogListView(ColourView, ListView):
    model = ChangeLog
    template_name = 'changelog.html'
    context_object_name = 'changes'
    ordering = ['-date_posted']


class ChangeLogDetailView(ColourView, DetailView):
    model = ChangeLog
    template_name = 'changelog-detail.html'


class ChangeLogCreateView(ColourView, CreateView):
    model = ChangeLog
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ChangeLogUpdateView(ColourView, UpdateView):
    model = ChangeLog
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ChangeLogDeleteView(ColourView, DeleteView):
    model = ChangeLog
    success_url = '/'
    template_name = 'blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
