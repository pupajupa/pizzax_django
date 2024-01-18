from django.shortcuts import render

from .models import Pizza

# Create your views here.
def pizzas_list_item(request,my_id):
    item = Pizza.objects.get(id=my_id)
    context = {
        'item':item    
    }
    return render(request, "myapp/detail_pizza.html",context)

def pizzas_list(request):
    items = Pizza.objects.all()
    context = {
        'items':items    
    }
    return render(request,"myapp/pizzas_list.html",context)