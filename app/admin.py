from django.contrib import admin

from app.models import *


class MemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_tag', 'user', 'private')
    list_filter = ('user', 'private')
    search_fields = ('title', 'user__username')
    readonly_fields = ('image_tag',)

# Register your models here.
admin.site.register(Tag)
admin.site.register(Meme, MemeAdmin)
