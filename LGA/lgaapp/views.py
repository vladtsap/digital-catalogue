from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Art, Book
from .forms import AddBook

from django.views import View
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from knowledge.models import Article


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

class ESearchView(View):
	template_name = 'search/index.html'
	def get(self, request, *args, **kwargs):
		context = {}
		question = request.GET.get('q')
		if question is not None:
			search_articles = Article.objects.filter(article_content__search=question)

				# формируем строку URL, которая будет содержать последний запрос
				# Это важно для корректной работы пагинации
				context['last_question'] = '?q=%s' % question

				current_page = Paginator(search_articles, 10)

				page = request.GET.get('page')
				try:
					context['article_lists'] = current_page.page(page)
				except PageNotAnInteger:
					context['article_lists'] = current_page.page(1)
				except EmptyPage:
					context['article_lists'] = current_page.page(current_page.num_pages)

			return render_to_response(template_name=self.template_name, context=context)