# users/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import user_login, user_register

app_name = 'users'

urlpatterns = [
    #path('', user_login, name='login'),  # Redirect to login page by default
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
]
