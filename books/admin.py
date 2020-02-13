from django.contrib import admin
from .models import Book, Review

# The place to register your models


class ReviewInline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    # determines which fields are displayed in the admin list for the Book object
    list_display = ("title", "author", "price")

    inlines = [
        ReviewInline,
    ]


admin.site.register(Book, BookAdmin)
