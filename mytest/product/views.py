from django.shortcuts import render, redirect
from .models import Product
from .forms import ProCreateForm

def create (request):
    if request.method == "POST":
        form = ProCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('pro-all')
    else:
        form = ProCreateForm()
    return render (request,'product/create.html',{"form":form})

def edit (request,id):
    ppt = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProCreateForm(request.POST,request.FILES,instance=ppt)
        if form.is_valid():
            form.save()
            return redirect ('pro-all')
    else:
        form = ProCreateForm(instance=ppt)
    return render (request,'product/edit.html',{"form":form})

def delete (request,id):
    Product.objects.get(id=id).delete()
    return redirect ('pro-all')

def all (request):
    return render (request,'product/all.html',{"pros":Product.objects.all()})