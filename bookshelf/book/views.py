from django.shortcuts import render
from django.db.models import Q

from .models import Book


def book_list(request):
    book_list = Book.objects.all()
    query = request.GET.get("q", "")
    books = Book.objects.all()

    if query:
        books = books.filter(
            Q(title__icontains=query)
            | Q(author__icontains=query)
            | Q(genre__icontains=query)
        )
    context = {"book_list": book_list, "books": books}
    return render(request, "book/book_list.html", context=context)
