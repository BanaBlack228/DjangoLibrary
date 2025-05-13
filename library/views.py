from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'library/create_author.html', {'form': form})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/create_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

