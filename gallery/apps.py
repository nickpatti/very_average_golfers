from django.apps import AppConfig

class GalleryConfig(AppConfig):
    name = 'gallery'
    verbose_name = 'Gallery'

    def ready(self):
        import gallery.signals
