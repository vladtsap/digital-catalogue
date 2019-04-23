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

def BookEdit(request, pk):
    if request.method == "POST":
        Book.objects.filter(slug=pk).delete()

        form = AddBook(request.POST)
        book = form.save(commit=False)
        book.save()
        return redirect('about-book', pk=book.slug)
    else:
        book = Book.objects.filter(slug=pk).get()
        form = AddBook(initial={'name': book.name,
                                'author': book.author,
                                'publication' : book.publication,
                                'description' : book.description,
                                'series' : book.series,
                                'personality' : book.personality,
                                'additional' : book.additional,
                                'isbn' : book.isbn,
                                'inventory_number' : book.inventory_number,
                                'cipher' : book.cipher,
                                'year' : book.year,
                                'place' : book.place,
                                'language' : book.language,
                                'country' : book.country,
                                'subject' : book.subject,
                                'art' : book.art,
                                'group' : book.group,
                                'slug' : book.slug
        })
        return render(request, 'about/edit.html', {'form': form})

def BookDelete(request, pk):
    if request.method == "DELETE":
        Book.objects.filter(slug=pk).delete()

    return redirect('index')


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


def SearchBox(request):
    return render_to_response('search/box.html')


def SearchResult(request):
    if request.GET:
        q = dict(request.GET)
        q = dict(map(cap, list(zip(list(q.keys()), q.values()))))

        try:
            if q['ser'] == '':
                q['ser'] = -1
            else:
                q['ser'] = int(q['ser'])
        except:
            pass

        try:
            if q['invnum'] == '':
                q['invnum'] = -1
            else:
                q['invnum'] = int(q['invnum'])
        except:
            pass

        try:
            if q['ciph'] == '':
                q['ciph'] = -1
            else:
                q['ciph'] = int(q['ciph'])
        except:
            pass

        years = []
        try:
            for i in range(int(q['yfr']), int(q['yto'])+1):
                years.append(str(i))
        except:
            pass

        books = Book.objects.all()

        books = books.filter(name__icontains=q['n'],
                            author__icontains=q['a'],
                            publication__icontains=q['publ'],
                            description__icontains=q['desc'],
                            personality__icontains=q['pers'],
                            place__icontains=q['plc'],
                            language__icontains=q['lang'],
                            country__icontains=q['cntr']
                            )

        if q['n'] != '':
            half = Book.objects.filter(name__istartswith=q['n'][:int(len(q['n']) / 2)])
            books = books | half

        if q['a'] != '':
            half = Book.objects.filter(author__istartswith=q['a'][:int(len(q['a']) / 2)])
            books = books | half

        if q['ser'] != -1:
            books = books.filter(series=q['ser'])

        if q['invnum'] != -1:
            books = books.filter(inventory_number=q['invnum'])

        if q['ciph'] != -1 :
            books = books.filter(cipher=q['ciph'])

        if years:
            books = books.filter(year__in=years)

        if q['isbn'] != '':
            books = books.filter(isbn__iexact=q['isbn'])

        if q['subj'] != '':
            books = books.filter(subject__name=q['subj'])

        if q['art'] != '':
            books = books.filter(art__name=q['art'])

        if q['gr'] != '':
            books = books.filter(group__name=q['gr'])

        return render_to_response('search/results.html',
                                  {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def bad_search(request):
    # The following line will raise KeyError if 'q' hasn't
    # been submitted!
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)
