from django.contrib import admin
from django.urls import path
from . import views
import api.views as views

urlpatterns = [
   path('books/', views.BookList.as_view(), name='book-list'),
]