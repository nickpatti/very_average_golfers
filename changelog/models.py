from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse


class ChangeLog(models.Model):
    title = models.CharField(max_length=50)
    date_posted = models.DateTimeField(default=timezone.now)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('changelog-detail', kwargs={'pk': self.pk})
