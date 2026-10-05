from django.urls import path
from .views import hello_view, over_hello

urlpatterns = [
    path('', hello_view, name='hello'),
    path("over/", over_hello, name="over"),
]


