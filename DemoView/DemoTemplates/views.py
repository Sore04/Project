from django.shortcuts import render, redirect
from .models import Item

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