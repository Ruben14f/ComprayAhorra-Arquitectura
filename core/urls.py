from django.urls import path
from core.auth_views.login import login_view
from core.auth_views.register import register_view
from core.views import home

urlpatterns = [
    path('', home, name='inicio'),
    path('login/', login_view, name='login'), 
    path('register/', register_view, name='register'), 
]