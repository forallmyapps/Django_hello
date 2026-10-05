# from django . contrib import admin
from django . urls import path
from budget.views import transacties, upload

urlpatterns = [
    path('', upload, name='upload'),
    path("transacties/", transacties, name="transacties"),
]

