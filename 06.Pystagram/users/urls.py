from django.urls import path
from .views import loginView, signupView, logoutView

urlpatterns = [
    path('login/', loginView, name="Login"),
    path('signup/', signupView, name="Signup"),
    path('logout/', logoutView, name="Logout"),
]
