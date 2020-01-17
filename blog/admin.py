from django.contrib import admin
from .models import Post, CompetitionsPost, TraditionsPost, SocialsPost, LinksPost, YearRoll, Members, EventRoll, TrophyPost, AllTimeRoll


# class TinyMCEAdmin(admin.ModelAdmin):
#     class Media:
#         js = ('/blog/static/js/tinymce/tiny_mce.js', '/blog/static/js/tinyce/textareas.js', )


admin.site.register(Post)

admin.site.register(CompetitionsPost)

admin.site.register(SocialsPost)

admin.site.register(TraditionsPost)

admin.site.register(LinksPost)

admin.site.register(EventRoll)

admin.site.register(YearRoll)

admin.site.register(AllTimeRoll)

admin.site.register(Members)

admin.site.register(TrophyPost)
