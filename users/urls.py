from django.urls import path, include

from . import views

app_name = "users"

urlpatterns = [
    path('loginPage/', views.loginPage, name="loginPage"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name="register"),
    path('home/', views.home, name="home")
]
