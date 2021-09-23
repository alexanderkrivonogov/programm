from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from comics_site.models import Category, Comic


def comics_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    comics = Comic.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        comics = comics.filter(category=category)
    return render(request,
                  'comics_site/comics/list.html',
                  {'category': category,
                   'categories': categories,
                   'comics': comics,
                   })


def comics_detail(request, id, slug):
    comics = get_object_or_404(
        Comic,
        id=id,
        slug=slug,
        available=True,
    )
    cart_comics_form = CartAddProductForm()
    return render(request, 'comics_site/comics/detail.html',
                  {'comics': comics,
                   'cart_comics_form': cart_comics_form}
    )
