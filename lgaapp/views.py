import os
import re

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from LGA.settings import DATABASES
from lgaapp.forms import SearchBook, AddBook
from lgaapp.models import Book


@require_http_methods(['GET'])
def index(request):
	books_length = Book.objects.count()
	return render(request, 'index.html', {'bookLength': books_length})


@require_http_methods(['GET', 'DELETE'])
def book_view_delete(request, pk):
	if request.method == 'GET':
		book = Book.objects.get(pk=pk)
		return render(request, 'about/book.html', {'book': book})
	elif request.method == 'DELETE':
		Book.objects.get(pk=pk).delete()
		return HttpResponse()


@require_http_methods(['GET', 'POST'])
def book_edit(request, pk):  # TODO: refactor
	if request.method == "POST":
		Book.objects.get(pk=pk).delete()

		form = AddBook(request.POST)
		book = form.save(commit=False)
		book.save()
		return redirect('about-book', pk=book.pk)
	else:
		book = Book.objects.get(pk=pk)
		form = AddBook(
			initial={
				'name': book.name,
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
			}
		)
		return render(request, 'about/edit.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def book_add(request):
	if request.method == "POST":
		form = AddBook(request.POST)
		book = form.save(commit=False)
		book.save()
		return redirect('about-book', pk=book.pk)
	else:
		form = AddBook()
		return render(request, 'about/add.html', {'form': form})


@require_http_methods(['GET'])
def search_box(request):
	form = SearchBook()
	return render(request, 'search/box.html', {'form': form})


def filter_books(query: dict) -> set[Book]:
	filter_query = {}

	if year_from := query.get('yfr'):
		filter_query['year__gte'] = int(year_from)

	if year_to := query.get('yto'):
		filter_query['year__lte'] = int(year_to)

	if subject := query.get('subj'):
		filter_query['subject'] = subject

	if art := query.get('art'):
		filter_query['art'] = art

	if group := query.get('gr'):
		filter_query['group'] = group

	if place := query.get('plc'):
		filter_query['place'] = place

	books = list(Book.objects.filter(**filter_query).all())

	if query.get('n'):
		temp = []
		for book in books:
			for elem in query['n'].split(' '):
				if elem.lower() in book.name.lower() and elem:
					temp.append(book)
		books = temp

	if query.get('a'):
		temp = []
		for book in books:
			for elem in query['a'].split(' '):
				if elem.lower() in book.author.lower() and elem:
					temp.append(book)
		books = temp

	if query.get('lang'):
		temp = []
		for book in books:
			for elem in re.split(r'\W+', query['lang']):
				if elem.lower() in book.language.lower() and elem:
					temp.append(book)
		books = temp

	if query.get('cntr'):
		temp = []
		for book in books:
			for elem in re.split(r'\W+', query['cntr']):
				if elem.lower() in book.country.lower() and elem:
					temp.append(book)
		books = temp

	if query.get('pers'):
		temp = []
		for book in books:
			for elem in query['pers'].split(' '):
				if elem.lower() in book.personality.lower() and elem:
					temp.append(book)
		books = temp

	if query.get('ser'):
		temp = []
		for book in books:
			for elem in query['ser'].split(' '):
				if elem.lower() in book.series.lower() and elem:
					temp.append(book)
		books = temp

	if query.get('invnum'):
		temp = []
		for book in books:
			if query['invnum'].lower() in book.inventory_number.lower():
				temp.append(book)
		books = temp

	if query.get('add'):
		temp = []
		for book in books:
			if query['add'].lower() in book.additional.lower():
				temp.append(book)
		books = temp

	if query.get('publ'):
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


@require_http_methods(['GET'])
def search_result(request):
	if args := request.GET:
		books = filter_books(args)
	else:
		books = Book.objects.all()

	paginator = Paginator(books, 15)
	paginated_books = paginator.get_page(args.get('page'))

	return render(
		request,
		'search/results.html',
		{
			'books': paginated_books,
			'first_page': args.get('page') is None,
		}
	)


@require_http_methods(['GET'])
def download_database(request):
	db_path = DATABASES['default']['NAME']

	with open(db_path, 'rb') as fh:
		response = HttpResponse(
			fh.read(),
			content_type='application/x-sqlite3',
		)
		response['Content-Disposition'] = 'inline; filename=' + os.path.basename(db_path)
	return response
