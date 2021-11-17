from django.urls import path

from . import views
from .views import search, detail, category

urlpatterns = [
    path('search/', search, name='search'),
    path('post/<slug:category_slug>/<slug:slug>/', detail, name='post_detail'),
    path('category/<slug:slug>/', category, name='category_detail')
]