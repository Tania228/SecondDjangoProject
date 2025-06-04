from django.test import TestCase
from .models import Book

class BookTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            name='Собачье сердце',
            author='Михаил Булгаков',
            pub_date='1925-03-07'
        )

    def test_book_creation(self):
        self.assertEqual(self.book.name, 'Собачье сердце')
        self.assertEqual(self.book.author, 'Михаил Булгаков')
        self.assertEqual(self.book.pub_date, '1925-03-07')