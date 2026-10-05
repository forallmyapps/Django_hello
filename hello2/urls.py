from django.urls import path
from .views import hello2_view

urlpatterns = [
    path('', hello2_view, name='hello2'),
]
