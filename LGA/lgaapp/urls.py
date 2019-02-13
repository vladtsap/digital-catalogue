from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^about/(?P<pk>([a-zA-Z]+[-]?)+(\d+[-]?)+)/$', views.BookView, name='about-book'),
	url(r'^about/new/$', views.BookAdd, name='add-book'),
    url(r'^search/$', views.Search, name='search-book'),
	url(r'^search-result/$', views.SearchResult, name='search-result'),
]