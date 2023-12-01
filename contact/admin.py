from django.contrib import admin
from .models import Contact, Category


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email','show',)
    ordering = ('-id',)
    search_fields = ('id', 'first_name', 'last_name',)
    list_editable = ('show',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    