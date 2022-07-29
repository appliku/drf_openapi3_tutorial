from wagtail.contrib.modeladmin.options import (ModelAdmin, modeladmin_register)

from .models import BlogTag


class BlogTagAdmin(ModelAdmin):
    model = BlogTag
    menu_label = 'Blog Tags'
    menu_icon = 'tag'
    list_display = ('name', 'h1',)
    list_filter = ('h1',)
    search_fields = ('h1',)

    def tag_name(self, obj):
        return obj.tag.name


modeladmin_register(BlogTagAdmin)
