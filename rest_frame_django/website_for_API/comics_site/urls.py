from django.urls import path, include
from .views import home

urlpatterns = [
    path('/comics', home, name='comics_l')
]