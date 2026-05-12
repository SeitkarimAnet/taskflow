from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


# форма регистрации
class RegisterForm(UserCreationForm):

    class Meta:

        model = CustomUser

        fields = [

            'username',

            'first_name',

            'last_name',

            'email',

            'phone',

            'avatar',

            'password1',

            'password2',
        ]


# форма редактирования профиля
class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = CustomUser

        fields = [

            'username',

            'first_name',

            'last_name',

            'email',

            'phone',

            'avatar',
        ]