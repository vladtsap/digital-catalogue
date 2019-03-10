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

def cap(x):
    if isinstance(x[1][0], str):
        return (x[0], x[1][0].capitalize())
    else:
        return (x[0], x[1][0])


def Search(request):
    return render_to_response('search.html')


def SearchResult(request):
    if request.GET:
        q = dict(request.GET)
        q = dict(map(cap, list(zip(list(q.keys()), q.values()))))
        try:
            q['ser'] = int(q['ser'])
        except:
            pass

        try:
            q['invnum'] = int(q['invnum'])
        except:
            pass

        try:
            q['ciph'] = int(q['ciph'])
        except:
            pass

        books = Book.objects.filter(name__icontains=q['n'],
                                    author__icontains=q['a']
                                    # publication__icontains=,
                                    # description__icontains=,
                                    # series__icontains=,
                                    # personality__icontains=,
                                    # additional__icontains=,
                                    # isbn__icontains=,
                                    # inventory_number__icontains=,
                                    # cipher__icontains=,
                                    # year__icontains=,
                                    # place__icontains=,
                                    # language__icontains=,
                                    # country__icontains=,
                                    # subject__icontains=,
                                    # art__icontains=,
                                    # group__icontains=
                                    )

        half = Book.objects.filter(name__istartswith=q['n'][:int(len(q) / 2)],
                                   author__istartswith=q['a'][:int(len(q) / 2)])
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
