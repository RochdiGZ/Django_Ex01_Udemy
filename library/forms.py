from django.forms import ModelForm

from library.models import Book


class AddBookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
