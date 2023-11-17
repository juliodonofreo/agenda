from django.contrib import admin

from contact import models


# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = "id", "first_name", "last_nome", "email",
    list_filter = "email",
    search_fields = "id", "first_name", "last_nome"
    list_per_page = 10
    list_max_show_all = 200
    list_editable = "email",
    list_display_links = ("id", "first_name")


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', "name")
    list_filter = ('id',)
    