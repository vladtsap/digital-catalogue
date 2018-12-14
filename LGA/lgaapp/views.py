from django.shortcuts import render, get_object_or_404
from .models import Art, Book
# Create your views here.


def BookView(request, art_slug=None):
    art = None
    arts = Art.objects.all()
    books = Book.objects.filter(id=1)

    if art_slug:
        art = get_object_or_404(Art, slug=art_slug)
        books = books.filter(art=art)

    return render(request, {
        'art': art,
        'arts': arts,
        'books': books
    })

#return render(request, 'search/index.html', {'arts':arts}) VLAD
