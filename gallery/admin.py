from django.contrib import admin
from models import Photo, Item


class PhotoInline(admin.TabularInline):  # admin.StackedInline
    model = Photo


class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)



