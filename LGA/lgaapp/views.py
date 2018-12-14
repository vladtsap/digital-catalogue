from django.shortcuts import render, get_object_or_404
from .models import Art, Book

def BookView(request):
    books = Book.objects.filter(id=1)
    arts = [Art.objects.get(pk=x['art']) for x in books.values('art')]

    return render(request, 'search/index.html', {
        'books': books,
        'arts': arts
    })
