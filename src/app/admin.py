from django.contrib import admin
from django.utils.safestring import mark_safe

from app.models import *
# Register your models here.

@admin.register(Web)
class WebAdmin(admin.ModelAdmin):
    list_display = ("image_view", "name", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"



@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"



@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ("libele", "description", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]



@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(AskService)
class AskServiceAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("image_view", "title", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"



@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("name", "link", 'publish')
    list_editable = ["publish"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("image_view", "name", "order",  "service_slug", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(SousService)
class SousServiceAdmin(admin.ModelAdmin):
    list_display = ("image_view", "name", "order", "price", "sous_service_slug", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]

    def image_view(self, obj):
        return mark_safe(f'<img src="{obj.picture.url}" style="height:100px; width:150px">')
    image_view.short_description = "Aperçu des images"


@admin.register(Commandes)
class CommandesAdmin(admin.ModelAdmin):
    list_display = ( "name", "phone", "service", "date_add", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "phone",  "email",'publish')
    list_editable = ["publish"]




@admin.register(Referencement)
class ReferencementAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "description", "keyword", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]



@admin.register(Prestatire)
class PrestatireAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "date_time", "publish")
    date_hierarchy = "date_add"
    list_per_page = 10
    list_editable = ["publish"]