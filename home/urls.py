from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('create/', create, name='create'),
    path('view/<slug>', view, name='view'),
    path('edit/<slug>', update, name='edit'),
    path('delete/<slug>', delete, name='delete'),
    path('search/', search, name='search'),
]