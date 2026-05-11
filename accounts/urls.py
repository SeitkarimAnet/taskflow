from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegisterView, logout_view


urlpatterns = [
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),
]