from django.urls import path

from django.contrib.auth import views as auth_views

from .views import (
    RegisterView,
    logout_view,
    ProfileUpdateView
)


urlpatterns = [

    # регистрация
    path(

        'register/',

        RegisterView.as_view(),

        name='register'
    ),

    # логин
    path(

        'login/',

        auth_views.LoginView.as_view(),

        name='login'
    ),

    # выход
    path(

        'logout/',

        logout_view,

        name='logout'
    ),

    # профиль пользователя
    path(

        'profile/',

        ProfileUpdateView.as_view(),

        name='profile-update'
    ),
]