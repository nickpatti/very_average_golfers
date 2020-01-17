from django.db import models
from colorful.fields import RGBColorField
from django.urls import reverse


class ColourScheme(models.Model):

    colour_choices = (
        ('green', 'Green on Green'),
        ('blue', 'Blue'),
        ('night', 'Dark'),
        ('classic', 'Classic'),
        ('metalic', 'Metalic'),
        ('sunburst', 'Sunburst')

    )

    colourpicker = models.CharField(max_length=20, choices=colour_choices, default='green')
    website_body_colour = RGBColorField(null=True, blank=True)


class Template(models.Model):

    template_choices = (
        ('old_template', 'Vag Society'),
        ('new_template', 'Vag Society 2.0')
    )

    template_picker = models.CharField(max_length=30, choices=template_choices, default='new_template', verbose_name='Choose A Template')

    def get_absolute_url(self):
        return reverse('template-change', kwargs={'pk': self.pk})
