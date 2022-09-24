from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from embed_video.admin import AdminVideoMixin
from.models import *


class HomevidAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Home,HomevidAdmin)

class ViralvidAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Viral,ViralvidAdmin)

class MovievidAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Movie,MovievidAdmin)


class ShortfilmvidAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Shortfilm,ShortfilmvidAdmin)


class WebshowvidAdmin(AdminVideoMixin,admin.ModelAdmin):
    pass
admin.site.register(Webshow,WebshowvidAdmin)



