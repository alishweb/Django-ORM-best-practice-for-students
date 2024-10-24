from django.urls import path
from .views import store_view

urlpatterns = [
    path('', store_view, name='store'),
]
