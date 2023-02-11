from django.shortcuts import render
from django.shortcuts import get_object_or_404

from library.forms import AddBookForm
from library.models import Book


def books(request):
    form = AddBookForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "library/index.html", context={"books": Book.objects.all(), "form": form})


def book(request, book_pk):
    article = get_object_or_404(Book, pk=book_pk)
    return render(request, "library/book.html", context={"book": article})
