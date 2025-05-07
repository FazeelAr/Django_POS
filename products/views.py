# product/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from django.contrib import messages

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def product_add(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        category = get_object_or_404(Category, id=category_id)

        product = Product.objects.create(
            name=name,
            category=category,
            price=price,
            stock=stock,
            description=description,
            image=image
        )
        product.save()
        messages.success(request, 'Product added successfully.')
        return redirect('product:product_list')

    return render(request, 'products/addProduct.html', {'categories': categories})

@login_required
def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.category = get_object_or_404(Category, id=request.POST.get('category'))
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.description = request.POST.get('description')
        product.save()

        messages.success(request, 'Product updated successfully.')
        return redirect('product:product_list')

    return render(request, 'products/product_form.html', {'product': product, 'categories': categories})

@login_required
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully.')
    return redirect('product:product_list')
