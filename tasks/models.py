from django.db import models
from django.conf import settings


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

    # описание
    description = models.TextField()

    # статус задачи
    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES
    )

    # приоритет
    priority = models.CharField(

        max_length=20,

        choices=PRIORITY_CHOICES
    )

    # владелец задачи
    owner = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE
    )

    # soft delete
    is_deleted = models.BooleanField(default=False)

    # дата создания
    created_at = models.DateTimeField(auto_now_add=True)

    # дедлайн задачи
    deadline = models.DateField(

        null=True,

        blank=True
    )

    def __str__(self):

        return self.title