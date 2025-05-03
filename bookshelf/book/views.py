from django.shortcuts import render, get_object_or_404
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

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {"book": book}
    return render(request, "book/book_detail.html", context)