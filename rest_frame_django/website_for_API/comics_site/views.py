from django.shortcuts import render
from .models import Category, Comics


def home(request):
    comics_list = Comics.objects.all()
    return render(request, 'page_category.html', dict(objects=comics_list))
