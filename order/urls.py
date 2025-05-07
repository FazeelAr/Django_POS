from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('create/', views.create_order, name='create_order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),  # optional
]
