from django import forms

from .models import Book

class AddBook(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('name',
		'author',
		'publication',
		'description',
		'series',
		'personality',
		'additional',
		'isbn',
		'inventory_number',
		'cipher',
		'year',
		'place',
		'language',
		'country',
		'subject',
		'art',
		'group',
		'slug',)