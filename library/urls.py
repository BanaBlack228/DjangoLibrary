from django.urls import path
from .views import create_author, author_list, create_book, book_list

urlpatterns = [
    path('authors/create/', create_author, name='create_author'),
    path('authors/', author_list, name='author_list'),
    path('books/create/', create_book, name='create_book'),
    path('books/', book_list, name='book_list'),
]
