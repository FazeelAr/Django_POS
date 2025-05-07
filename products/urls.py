# product/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'product'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.product_add, name='product_add'),
    path('edit/<int:product_id>/', views.product_edit, name='product_edit'),
    path('delete/<int:product_id>/', views.product_delete, name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
