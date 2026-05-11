from django.db import models
from django.conf import settings

# работа с датой
from datetime import date


# модель задачи
class Task(models.Model):

    # варианты статуса
    STATUS_CHOICES = [

        ('new', 'New'),

        ('progress', 'In Progress'),

        ('done', 'Done'),
    ]

    # варианты приоритета
    PRIORITY_CHOICES = [

        ('low', 'Low'),

        ('medium', 'Medium'),

        ('high', 'High'),
    ]

    # название задачи
    title = models.CharField(max_length=255)

    # описание задачи
    description = models.TextField()

    # статус
    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES
    )

    # приоритет
    priority = models.CharField(

        max_length=20,

        choices=PRIORITY_CHOICES
    )

    # пользователь
    owner = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE
    )

    # soft delete
    is_deleted = models.BooleanField(default=False)

    # дата создания
    created_at = models.DateTimeField(auto_now_add=True)

    # дедлайн
    deadline = models.DateField(

        null=True,

        blank=True
    )

    # цвет задачи по дедлайну
    def get_deadline_color(self):

        # если дедлайна нет
        if not self.deadline:

            return 'secondary'

        # сколько дней осталось
        days_left = (self.deadline - date.today()).days

        # просроченная задача
        if days_left < 0:

            return 'dark'

        # очень срочно
        elif days_left <= 2:

            return 'danger'

        # скоро дедлайн
        elif days_left <= 5:

            return 'warning'

        # времени еще много
        else:

            return 'success'

    # отображение названия задачи
    def __str__(self):

        return self.title