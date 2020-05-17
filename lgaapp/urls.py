from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/(?P<pk>(.*?)+)/$', views.book_view, name='about-book'),
	url(r'^about/(?P<pk>(.*?)+)/edit', views.book_edit, name='edit-book'),
	url(r'^about/(?P<pk>(.*?)+)/delete', views.book_delete, name='delete-book'),
	url(r'^add/$', views.book_add, name='add-book'),
	url(r'^search/$', views.search_box, name='search-book'),
	url(r'^search/result/$', views.search_result, name='search-result'),
]
