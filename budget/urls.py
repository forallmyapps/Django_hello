# from django . contrib import admin
from django . urls import path
from budget.views import transacties, upload, grafiek

urlpatterns = [
    path('', upload, name='upload'),
    path('transacties/', transacties, name='transacties'),
    path('grafiek/', grafiek, name='grafiek'),
]

