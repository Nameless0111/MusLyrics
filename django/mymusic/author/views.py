from django.shortcuts import render, get_object_or_404
from .models import Author

def author_detail(request, name):
    author = get_object_or_404(Author, name=name)
    return render(request, 'author/author_detail.html', {'author': author})