from django.conf.urls import urls
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
]