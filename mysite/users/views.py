from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import new_user_form

def register(request):
    if request.method == "POST":
        form = new_user_form(request.POST)
        if form.is_valid():
           user=form.save() 
           login(request,user)
           return redirect("myapp:pizzas_list")
    form = new_user_form()
    context = {
        'form':form
        }
    return render(request,'users/register.html',context)
