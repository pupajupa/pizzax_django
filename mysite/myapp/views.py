from django.shortcuts import render, redirect

from .models import Pizza


# Create your views here.
def pizzas_list_item(request, my_id):
    item = Pizza.objects.get(id=my_id)
    context = {"item": item}
    return render(request, "myapp/detail_pizza.html", context)


def pizzas_list(request):
    items = Pizza.objects.all()
    context = {"items": items}
    return render(request, "myapp/pizzas_list.html", context)


def add_pizza(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES.get("upload")
        item = Pizza(name=name, price=price, description=description, image=image)
        item.save()
    return render(request, "myapp/add_pizza.html")


def update_pizza_item(request, my_id):
    item = Pizza.objects.get(id=my_id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get("upload", item.image)
        item.save()
        return redirect("/myapp/")
    context = {"item": item}
    return render(request, "myapp/update_pizza_item.html", context)


def delete_pizza_item(request, my_id):
    item = Pizza.objects.get(id=my_id)
    if request.method == "POST":
        item.delete()
        return redirect("/myapp/")
    context = {"item": item}
    return render(request, "myapp/delete_pizza_item.html", context)
