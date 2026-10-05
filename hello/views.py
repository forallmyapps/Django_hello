from django.shortcuts import render

# from django.http import HttpResponse
# Create your views here.

def hello_view(request):
    ctx = {"body_title": "De title (in de body)", "head_title": "First Django App",  "items": ["Python", "Django", "ORM"]}
    return render(request, "hello/home.html", ctx)

def over_hello(request):
    ctx = {"body_title": "Over deze site", "head_title": "Over" }
    return render(request, "hello/over.html", ctx)


