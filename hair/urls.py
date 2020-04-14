from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service', views.service, name='service'),
    path('book', views.book, name='book'),
    path('time', views.time, name='time'),
]