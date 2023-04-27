from django.contrib import admin
from .models import Contacts

class AdminContacts(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'cpf', 'active']
    search_fields = ['name']
    list_filter = ['active']
    list_display_links = ['name']

admin.site.register(Contacts, AdminContacts)



