import re

from lgaapp.models import Book


def filter_books(query: dict) -> list[Book]:
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

	books = set(Book.objects.filter(**filter_query).all())
	to_delete = set()

	for book in books:

		# case-insensitive separated filter
		for key, book_property in {
			'n': book.name,
			'a': book.author,
			'lang': book.language,
			'cntr': book.country,
			'pers': book.personality,
			'ser': book.series,
		}.items():
			if value := query.get(key):
				is_searched = False
				for elem in filter(None, re.split(r'\W+', value)):
					if elem.lower() in book_property.lower():
						is_searched = True

				if not is_searched:
					to_delete.add(book)

		# case-sensitive joined filter
		for key, book_property in {
			'invnum': book.inventory_number,
			'add': book.additional,
			'publ': book.publication,
		}.items():
			if value := query.get(key):
				if value.lower() not in book_property.lower():
					to_delete.add(book)

	books = books.difference(to_delete)

	return list(books)
