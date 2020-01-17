from django.contrib import admin
from .models import ColourScheme, Template


class ColourAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(ColourScheme)

admin.site.register(Template)
