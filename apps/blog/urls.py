from django.urls import path

from apps.blog.views import listview_post

urlpatterns = [
    path('', listview_post, name='listview_post'),
]