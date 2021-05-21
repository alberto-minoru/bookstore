from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    model = Book
    # context_object_name = 'book_list'  # Opcional se manter este formato de nome (nome_obj)_list
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
