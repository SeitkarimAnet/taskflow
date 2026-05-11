from django.contrib import admin

from .models import CustomUser

# подключаем модель пользователя в админ панель
admin.site.register(CustomUser)