from django.urls import path
from .views import userlogin, userlogout, userregister

app_name = "accounts"

urlpatterns = [
    path('register', userregister, name='register'),
    path('login', userlogin, name='login'),
    path('logout', userlogout, name='logout'),
]
