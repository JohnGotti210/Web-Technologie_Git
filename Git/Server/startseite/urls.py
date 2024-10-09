from django.urls import path
from .views import home, register_user, login_user
from .views import register_user, login_user

urlpatterns = [
    path('', home, name='home'),  
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
]
