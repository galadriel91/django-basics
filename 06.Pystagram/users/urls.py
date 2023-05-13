from django.urls import path
from .views import login_view, signup_view, logout_view

urlpatterns = [
    path('login/', login_view, name='Login'),
    path('signup/', signup_view, name='Signup'),
    path('logout/', logout_view, name='Logout'),
]
