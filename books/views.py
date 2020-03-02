from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin)
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book

# Create your views here.


class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'  # new. overrides 'object_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'  # new.  overrides 'object'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'  # new for loginrequiredmixin
    # new for permission required (name of the permission we created)
    permission_required = 'books.special_status'
