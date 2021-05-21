from django.views.generic import ListView
from .models import Book


class BookListView(ListView):
    model = Book
    # context_object_name = 'book_list'  # Opcional se manter este formato de nome (nome_obj)_list
    template_name = 'books/book_list.html'
