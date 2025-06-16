from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from order.models import Order
from products.models import Product
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def dashboard_home(request):
    now = timezone.now()
    today = now.date()
    today_sales = sum(order.total_price() for order in Order.objects.filter(
        status='completed', created_at__date=today))

    recent_orders = Order.objects.filter(status='completed').order_by('-created_at')[:5]
    total_products = Product.objects.count()
    total_users = User.objects.count()
    total_products = Product.objects.count()
    
    # Example: Sales in last 7 days
    week_ago = timezone.now() - timedelta(days=7)
    recent_sales = sum(order.total_price() for order in Order.objects.filter(created_at__gte=week_ago))

    low_stock_products = Product.objects.filter(stock__lt=10)

    return render(request, 'dashboard/dashboard_home.html', {
        'today_sales': today_sales,
        'recent_orders': recent_orders,
        'total_products': total_products,
        'low_stock_products': low_stock_products,
        'total_users':total_users,
        'recent_sales':recent_sales
    })
