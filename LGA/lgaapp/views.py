from django.shortcuts import render, get_object_or_404
from .models import Art, Book

def BookView(request, pk):
    books = Book.objects.filter(id=pk)
    arts = [Art.objects.get(pk=x['art']) for x in books.values('art') if x['art'] != None]
    # if Art.objects.get(pk=books.values('art')['art']) != None:
    #     arts = [Art.objects.get(pk=x['art']) for x in books.values('art')]

    return render(request, 'about/book.html', {
        'books': books,
        'arts': arts
    })

def Index(request):
    return render(request, 'index.html')