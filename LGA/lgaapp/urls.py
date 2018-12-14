from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^about/(?P<pk>[0-9]+)/$', views.BookView, name='about-book'),
]