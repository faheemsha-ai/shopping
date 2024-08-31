from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = "index"),
    path("reg",views.signup, name="signup"),
    path("product",views.product, name="product"),
    path("cart",views.view_cart, name="cart"),
]