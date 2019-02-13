from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Art, Book
from .forms import AddBook


def BookView(request, pk):
    books = Book.objects.filter(slug=pk)
    # arts = [Art.objects.get(pk=x['art']) for x in books.values('art') if x['art'] != None]
    # if Art.objects.get(pk=books.values('art')['art']) != None:
    #     arts = [Art.objects.get(pk=x['art']) for x in books.values('art')]

    return render(request, 'about/book.html', {
        'books': books,
        # 'arts': arts
    })


def Index(request):
    return render(request, 'index.html')


def BookAdd(request):
    if request.method == "POST":
        form = AddBook(request.POST)
        book = form.save(commit=False)
        book.save()
        return redirect('about-book', pk=book.slug)
    else:
        form = AddBook()
        return render(request, 'about/add.html', {'form': form})


# def search(request):
#     if request.method == 'GET': # this will be GET now
#         book_name =  request.GET.get('search') # do some research what it does
#         try:
#             status = Book.objects.filter() # filter returns a list so you might consider skip except par
#         except:
#             raise ValueError
#         return render(request,"search/console.html",{"books":status})
#     else:
#         return render(request,"search/console.html",{})

def Search(request):
    return render_to_response('search.html')


def SearchResult(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q'].capitalize()
        books = Book.objects.filter(name__icontains=q)
        half = Book.objects.filter(name__istartswith=q[:int(len(q)/2)])
        books = books | half
        return render_to_response('search_results.html',
                                  {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def bad_search(request):
    # The following line will raise KeyError if 'q' hasn't
    # been submitted!
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)
