from django.contrib import admin
from .models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # determines which fields are displayed in the admin list for the Book object
    list_display = ("title", "author")


admin.site.register(Book, BookAdmin)
