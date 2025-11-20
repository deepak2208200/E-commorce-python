from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:id>/", views.product_detail, name="product_detail"),
    path("category/<int:category_id>/", views.category_products, name="category_products"),
]
