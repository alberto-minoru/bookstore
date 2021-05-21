from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):

    def setUp(self) -> None:
        self.book = Book.objects.create(
            title='Marley e Eu',
            author='John Grogan',
            price='35.90',
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Marley e Eu')
        self.assertEqual(f'{self.book.author}', 'John Grogan')
        self.assertEqual(f'{self.book.price}', '35.90')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Marley e Eu')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Marley e Eu')
        self.assertTemplateUsed(response, 'books/book_detail.html')
