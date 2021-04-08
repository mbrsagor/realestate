from django.contrib import admin

from leads.models.book import Book
from leads.models.lead import Lead

admin.site.register(Lead)
admin.site.register(Book)
