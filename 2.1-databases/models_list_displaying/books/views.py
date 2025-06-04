from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from books.models import Book


def books_view(request):
    """Страница с каталогом книг"""

    template = 'books/books_list.html'
    book = Book.objects.all()
    context = {
        'book': book
    }
    return render(request, template, context)

def book_for_the_date(request, name):
    """Страница выбранной книги"""

    template = 'books/one_book.html'

    book = get_object_or_404(Book, name=name)

    pub_date = book.pub_date.date()

    all_books = Book.objects.all()
    all_dates = sorted(set(book.pub_date.date() for book in all_books))

    current_index = all_dates.index(pub_date)

    previous_date = all_dates[current_index - 1] if current_index > 0 else None
    next_date = all_dates[current_index + 1] if current_index < len(all_dates) - 1 else None

    books_today = all_books.filter(pub_date__date=pub_date)

    paginator = Paginator(books_today, 1)  # 1 книга на странице
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'book': book,
        'previous_date': previous_date,
        'next_date': next_date,
        'page': page
    }

    return render(request, template, context)