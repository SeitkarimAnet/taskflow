from django.urls import path

from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [

    # главная страница
    path(
        '',
        TaskListView.as_view(),
        name='task_list'
    ),

    # создание задачи
    path(
        'task/create/',
        TaskCreateView.as_view(),
        name='task_create'
    ),

    # редактирование
    path(
        'task/<int:pk>/update/',
        TaskUpdateView.as_view(),
        name='task_update'
    ),

    # удаление
    path(
        'task/<int:pk>/delete/',
        TaskDeleteView.as_view(),
        name='task_delete'
    ),
]