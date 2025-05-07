# # users/forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'role', 'password1', 'password2']

# # users/forms.py

# class CustomAuthenticationForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs = {
#             'class': 'form-input',
#             'placeholder': 'Enter your Email',
#             'id': 'username',
#             'name': 'username'
#         }
#         self.fields['password'].widget.attrs = {
#             'class': 'form-input',
#             'placeholder': 'Enter your Password',
#             'id': 'password',
#             'name': 'password'
#         }

