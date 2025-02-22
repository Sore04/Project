from django.shortcuts import render, redirect
from .models import Item, Book

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


def page2(request):
    return render(request, 'page2.html')


def save(request):

    # Get form data
    name = request.POST['name']
    description = request.POST['description']

    newItem = Item(name = name, description = description)
    newItem.save()

    return redirect('/demotemplates/')

def edit(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'page2.html', {'item': item})


def update(request, id):
    item = Item.objects.get(id=id)
    item.name = request.POST['name']
    item.description = request.POST['description']
    item.save()

    items = Item.objects.all()
    return redirect('/demotemplates/')

def delete(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('/demotemplates/')








def insert(request):
    books = Book.objects.all()
    return render(request, 'insert.html', {'books': books})


def saveBook(request):
    title = request.POST['title']
    author = request.POST['author']

    newBook = Book(title=title, author=author)
    newBook.save()

    return redirect('/demotemplates/insert/')

def editBook(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'editBook.html', {'book': book})

def updateBook(request, id):
    book = Book.objects.get(id=id)
    book.title = request.POST['title']
    book.author = request.POST['author']
    book.save()

    return redirect('/demotemplates/insert/')

def deleteBook(request, id):
    book = Book.objects.get(id=id)
    book.delete()

    return redirect('/demotemplates/insert/')