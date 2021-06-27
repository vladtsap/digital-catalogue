from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/<int:pk>/', views.book_view_delete, name='about-book'),
	path('about/<int:pk>/edit/', views.book_edit, name='edit-book'),
	path('add/', views.book_add, name='add-book'),
	path('search/', views.search_box, name='search-book'),
	path('search/result/', views.search_result, name='search-result'),
]
