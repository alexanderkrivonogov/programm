from time import timezone

from django.shortcuts import render, redirect
from django.views.generic import View
from catalog.forms import ProductForm
from catalog.models import Category


def home_page(request):
    return render(request, 'devAid-v1.1/index.html')


def home(request):
    store_list = Category.objects.all()
    return render(request, 'home.html', dict(objects=store_list))


def post_new(request):
    err = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            err = "Форма была неверной"
    form = ProductForm()
    data = {
        'form': form,
        'err': err
    }
    return render(request, 'index.html', data)
