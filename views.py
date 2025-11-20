from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Home page
def home(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})

# Product details
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "store/product_detail.html", {"product": product})

# Products by category
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, "store/category_products.html", {"category": category, "products": products})
