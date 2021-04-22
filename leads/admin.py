from django.contrib import admin

from leads.models.book import Book
from leads.models.lead import Lead
from leads.models.member import Member


class LeadManager(admin.ModelAdmin):
    # list_display = ['id', 'title', 'author']
    search_fields = ['id', 'title']
    # list_editable = ['title', ]
    list_per_page = 8
       
admin.site.register(Lead, LeadManager)

class BookManager(admin.ModelAdmin):
    # list_display = ['id', 'name', 'author', 'email', 'comments', 'messages']
    search_fields = ['email', 'name']
    # list_editable = ['name', 'email']
    list_per_page = 8

admin.site.register(Book, BookManager)

admin.site.register(Member)
