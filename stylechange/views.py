from django.shortcuts import render
from .models import ColourScheme
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.views import ColourView
from .models import Template


def colourchange(request):
    choice = ColourScheme.objects.all().first()


class TemplateChange(ColourView, UpdateView):
    model = Template
    fields = ['template_picker']
    template_name = 'blog/post_form.html'
