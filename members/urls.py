from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_form, name='hello-form'),
    path('nieuw/', views.member_create, name='member-create'),
    path('succes/', views.member_success, name='member-success'),
    path('lijst/', views.member_list, name='member-list'),
]
