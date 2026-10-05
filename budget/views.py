# from django.http import HttpResponse
from django.shortcuts import render

def transacties(request):
    return render(request, "budget/transacties.html")

#    return HttpResponse("Hello budget")
