from django.shortcuts import render, get_object_or_404, redirect
from .models import Art, Book
from .forms import AddBook

def BookView(request, pk):
	books = Book.objects.filter(slug=pk)
	#arts = [Art.objects.get(pk=x['art']) for x in books.values('art') if x['art'] != None]
	# if Art.objects.get(pk=books.values('art')['art']) != None:
	#     arts = [Art.objects.get(pk=x['art']) for x in books.values('art')]

	return render(request, 'about/book.html', {
		'books': books,
		#'arts': arts
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