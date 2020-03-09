from django.shortcuts import render, redirect
from .models import Category
from .forms import CatCreateForm

def create (request):
    if request.method == "POST":
        form = CatCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cat-all')
    else:
        form = CatCreateForm()
    return render (request,'category/create.html',{"form":form})


def edit (request,id):
    ppt = Category.objects.get(id=id)
    if request.method== "POST":
        form = CatCreateForm(request.POST,instance=ppt)
        if form.is_valid():
            form.save()
            return redirect ('cat-all')
    else:
        form = CatCreateForm(instance=ppt)
    return render (request,'category/edit.html',{"form":form})


def delete (request,id):
    Category.objects.get(id=id).delete()
    return redirect ('cat-all')


def all (request):
    return render (request,'category/all.html', {"cats":Category.objects.all()})