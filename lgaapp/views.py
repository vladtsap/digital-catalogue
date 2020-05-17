from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Book
from .forms import AddBook, SearchBook
import re


def book_view(request, pk):
	books = Book.objects.filter(pk=pk)
	return render(request, 'about/book.html', {'books': books})


def book_edit(request, pk):
	if request.method == "POST":
		Book.objects.filter(pk=pk).delete()

		form = AddBook(request.POST)
		book = form.save(commit=False)
		book.save()
		return redirect('about-book', pk=book.pk)
	else:
		book = Book.objects.filter(pk=pk).get()
		form = AddBook(initial={'name': book.name,
								'author': book.author,
								'publication': book.publication,
								'description': book.description,
								'series': book.series,
								'personality': book.personality,
								'additional': book.additional,
								'isbn': book.isbn,
								'inventory_number': book.inventory_number,
								'cipher': book.cipher,
								'year': book.year,
								'place': book.place,
								'language': book.language,
								'country': book.country,
								'subject': book.subject,
								'art': book.art,
								'group': book.group,
								'slug': book.slug
								})
		return render(request, 'about/edit.html', {'form': form})


def book_delete(request, pk):
	Book.objects.filter(pk=pk).delete()


def index(request):
	books = Book.objects.all()
	booksLength = len(books)
	return render(request, 'index.html', {'bookLength': booksLength})


def book_add(request):
	if request.method == "POST":
		form = AddBook(request.POST)
		book = form.save(commit=False)
		book.save()
		return redirect('about-book', pk=book.pk)
	else:
		form = AddBook()
		return render(request, 'about/add.html', {'form': form})


def search_box(request):
	form = SearchBook()
	return render(request, 'search/box.html', {'form': form})


def cap(x):
	return x[0], x[1][0]


def filtering_search(query):
	books = Book.objects.all()

	try:
		years = []
		for i in range(int(query['yfr']), int(query['yto']) + 1):
			years.append(str(i))
		books = books.filter(year__in=years)
	except:
		pass

	if query['subj']:
		books = books.filter(subject=query['subj'])

	if query['art']:
		books = books.filter(art=query['art'])

	if query['gr']:
		books = books.filter(group=query['gr'])

	if query['plc']:
		books = books.filter(place=query['plc'])

	books = list(books)

	if query['n']:
		temp = []
		for book in books:
			for elem in query['n'].split(' '):
				if elem.lower() in book.name.lower() and elem:
					temp.append(book)
		books = temp

	if query['a']:
		temp = []
		for book in books:
			for elem in query['a'].split(' '):
				if elem.lower() in book.author.lower() and elem:
					temp.append(book)
		books = temp

	if query['lang']:
		temp = []
		for book in books:
			for elem in re.split(r'\W+', query['lang']):
				if elem.lower() in book.language.lower() and elem:
					temp.append(book)
		books = temp

	if query['cntr']:
		temp = []
		for book in books:
			for elem in re.split(r'\W+', query['cntr']):
				if elem.lower() in book.country.lower() and elem:
					temp.append(book)
		books = temp

	if query['pers']:
		temp = []
		for book in books:
			for elem in query['pers'].split(' '):
				if elem.lower() in book.personality.lower() and elem:
					temp.append(book)
		books = temp

	if query['ser']:
		temp = []
		for book in books:
			for elem in query['ser'].split(' '):
				if elem.lower() in book.series.lower() and elem:
					temp.append(book)
		books = temp

	if query['invnum']:
		temp = []
		for book in books:
			if query['invnum'].lower() in book.inventory_number.lower():
				temp.append(book)
		books = temp

	if query['add']:
		temp = []
		for book in books:
			if query['add'].lower() in book.additional.lower():
				temp.append(book)
		books = temp

	if query['publ']:
		temp = []
		for book in books:
			if query['publ'].lower() in book.publication.lower():
				temp.append(book)
		books = temp

	# delete duplicates
	result = []
	for item in books:
		if item not in result:
			result.append(item)

	return result


def search_result(request):
	if request.GET:
		q = dict(request.GET)
		q = dict(map(cap, list(zip(list(q.keys()), q.values()))))

		books = filtering_search(q)

		books_count = books.__len__()
		paginator = Paginator(books, 10)

		firstPage = False
		prev_page = False
		next_page = False

		try:
			books = paginator.get_page(q['page'])
		except:
			firstPage = True
			q['page'] = 1
			books = paginator.get_page(1)

		if int(q['page']) > 1:
			prev_page = True

		if paginator.num_pages - int(q['page']) > 0:
			next_page = True

		return render_to_response('search/results.html',
								  {'books': books, 'query': q, 'books_count': books_count,
								   'prev_page': prev_page, 'next_page': next_page, 'firstPage': firstPage})
	else:
		return HttpResponse('Please submit a search term.')


def bad_search(request):
	message = 'You searched for: %r' % request.GET['q']
	return HttpResponse(message)
