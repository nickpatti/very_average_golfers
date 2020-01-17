from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


class MediaRootS3BotoStorage(S3BotoStorage):
    """
    Storage for uploaded media files.
    """

    def __init__(self, *args, **kwargs):
        kwargs['location'] = 'media'
        super(MediaRootS3BotoStorage, self).__init__(*args, **kwargs)
