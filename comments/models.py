from django.db import models
from django.contrib.auth.models import User
from gallery.models import Image


class ImageComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Image, on_delete=models.CASCADE)
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default='')
    object_id = models.PositiveIntegerField(default=1)
    # content_object = GenericForeignKey('content_type', 'object_id')
    content = models.TextField(verbose_name="New Comment")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)
