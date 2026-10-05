from django.shortcuts import render

from django.http import HttpResponse

def hello2_view(request):
    ctx = {"body_title": "De 2e django app", "head_title": "Second Django App",  "items": ["Python", "Django", "ORM"]}
    return render(request, "hello2/home.html", ctx)

def over_hello(request):
    ctx = {"body_title": "Over deze tweede site", "head_title": "Over" }
    return render(request, "hello2/over.html", ctx)

