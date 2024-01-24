from django.urls import path
from myapp import views
app_name = "myapp"

urlpatterns = [
    path("",views.pizzas_list),
    path("<int:my_id>/",views.pizzas_list_item,name="detail_pizza"),
    path("addpizza/",views.add_pizza,name="add_pizza"),
    path("updatepizzaitem/<int:my_id>/",views.update_pizza_item,name="update_pizza_item"),
]
   