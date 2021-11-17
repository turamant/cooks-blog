from django.urls import path

from apps.core.views import frontpage, about

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('about/', about, name='about')
]