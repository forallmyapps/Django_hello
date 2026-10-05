
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MemberForm

def member_create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            # joined_date wordt automatisch gezet door auto_now_add
            member = form.save()
            return redirect("member-success")
    else:
        form = MemberForm()
        ctx = {"body_title": "Create member", "head_title": "Create member", "form": form }
        return render(request, "members/member_form.html", ctx)


# def hello2_view(request):
#     ctx = {"body_title": "De 2e django app", "head_title": "Second Django App",  "items": ["Python", "Django", "ORM"]}
#     return render(request, "hello2/home.html", ctx)

def member_success(request):
    return render(request, "members/member_success.html")


def hello_form(request):
    message = None
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if name:
            message = f"Hallo, { name }!"
        else:
            message = "Vul een naam in."

    return render(request, "members/hello_form.html", {"message": message})

def member_list(request):
    from .models import Member
    members = Member.objects.order_by('-joined_date')

    return render(request, "members/member_list.html", {"members": members})
