# Generated by Django 2.2.1 on 2019-12-09 20:15

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stylechange', '0005_auto_20190523_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='colourscheme',
            name='website_body_colour',
            field=colorful.fields.RGBColorField(blank=True, null=True),
        ),
    ]
