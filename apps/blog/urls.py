from django.urls import path

from apps.blog.views import detail, category, search

urlpatterns = [
    path('search/', search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', detail, name='post_detail'),
    path('<slug:slug>/', category, name='category_detail')
]