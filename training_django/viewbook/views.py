# from django.http import request
from django.shortcuts import render
from django.views.generic import ListView
from viewbook.models import Book
from django.core.paginator import Paginator


class ViewListBook(ListView):
    model = Book
    paginate_by = 2

    def get_queryset(self):  # Get data from database and setting, this is stronger get_context_data
        key_word = self.request.GET.get('q')
        if key_word:
            return Book.objects.filter(name__icontains=key_word)
        else:
            return Book.objects.all()