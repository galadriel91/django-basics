from django.urls import path
from .views import loginView, signupView

urlpatterns = [
    path('login/', loginView, name="Login"),
    path('signup/', signupView, name="Signup"),
]
