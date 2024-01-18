from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns = [
    path("",views.pizzas_list),
    path("<int:my_id>/",views.pizzas_list_item,name="detail_pizza"),
]
   