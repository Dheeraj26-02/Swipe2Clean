from django.contrib import admin
from . models import Note
from django.utils.html import format_html
from .models import UploadImage
# from . models import BusinessPage
admin.site.site_header = "Swipe2Clean Admin's"
# admin.site.register(Note)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id','userr','uemail','ucomment')

@admin.register(UploadImage)
class UploadImageAdmin(admin.ModelAdmin):
    list_display = ('id','okmail','addr','comment','num','cause_image')

    def cause_image(slef, obj):
        return format_html('<img src="{0}" width="auto" height="150px">'.format(obj.image.url))

