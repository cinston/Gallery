from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^location/(\d+)', views.location, name='location'),
    url(r'^results/', views.search, name='search')

]