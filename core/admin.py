from django.contrib import admin
from core.models import *
from django.utils.html import mark_safe
# Register your models here.

@admin.register(Comment)
class CatagoryAdmin(admin.ModelAdmin):
    list_display=("author","text",)
    search_filter=("author",)
    list_editable=("author",)
    list_display_links=("text",)
    radio_filds=("post",)


    def image_tag(self, obj):
        return mark_safe('<img src="%s" width="100" height="100"/>' %(obj.image.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
admin.site.register(Category)
admin.site.register(Post)