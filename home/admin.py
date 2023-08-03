from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'Image', 'email', 'phone']


admin.site.register(Customer, CustomerAdmin)
