from django.contrib import admin
from phones.models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'release_date']
    list_filter = ['name', 'price', 'release_date']
    list_display_links = ['name']
