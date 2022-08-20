from django.shortcuts import render, get_object_or_404

from .models import Category, Product

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    return render(request, 'store/category_detail.html', {
        'category': category,
        'products': products
    })

def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'store/product_detail.html', {
        'product': product
    })