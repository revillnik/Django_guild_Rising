from django.contrib import admin
from .models import all_information


@admin.register(all_information)
class all_information_admin(admin.ModelAdmin):
    fields = ["title", "content", "slug", "photo", "link"]
    list_display = ("title", "slug", "photo")
    list_display_links = ("title",)
    prepopulated_fields = {"slug": ("title",)}
