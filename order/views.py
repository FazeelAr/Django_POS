# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem
from cart.models import Cart
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order/order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order/order_detail.html', {'order': order})

@login_required
def create_order(request):
    cart = Cart.objects.filter(user=request.user)
    if not cart.exists():
        return redirect('cart:view_cart')

    order = Order.objects.create(user=request.user, created_at=timezone.now())
    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
    cart.delete()  # clear cart
    return redirect('order:order_detail', order_id=order.id)

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()
    return redirect('order:order_list')
