from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import new_user_form, update_profile_form
from django.contrib.auth.decorators import login_required
from .models import Profile


def register(request):
    if request.method == "POST":
        form = new_user_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("myapp:pizzas_list")
    form = new_user_form()
    context = {"form": form}
    return render(request, "users/register.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        contact_number = request.POST.get("number")
        name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        image = request.FILES["upload"]
        item = Profile(
            contact_number=contact_number, image=image, name=name, last_name=last_name
        )
        item.save()
        return redirect("/myapp/")
    return render(request, "users/profile.html")
