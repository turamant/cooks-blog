from django.urls import path



urlpatterns = [
    path('', listview_posts, name='listview_post'),
]