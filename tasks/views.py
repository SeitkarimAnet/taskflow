from django.urls import reverse_lazy

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

from .models import Task


# список задач
class TaskListView(LoginRequiredMixin, ListView):

    model = Task

    template_name = 'tasks/task_list.html'

    # показываем только задачи текущего пользователя
    def get_queryset(self):

        return Task.objects.filter(
            owner=self.request.user,
            is_deleted=False
        )


# страница одной задачи
class TaskDetailView(LoginRequiredMixin, DetailView):

    model = Task

    template_name = 'tasks/task_detail.html'


# создание задачи
class TaskCreateView(LoginRequiredMixin, CreateView):

    model = Task

    fields = [
        'title',
        'description',
        'status',
        'priority',
        'deadline'
    ]

    template_name = 'tasks/task_form.html'

    success_url = reverse_lazy('task_list')

    # автоматически привязываем задачу к пользователю
    def form_valid(self, form):

        form.instance.owner = self.request.user

        return super().form_valid(form)


# редактирование задачи
class TaskUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView
):

    model = Task

    fields = [
        'title',
        'description',
        'status',
        'priority',
        'deadline'
    ]

    template_name = 'tasks/task_form.html'

    success_url = reverse_lazy('task_list')

    # проверяем владелец ли это
    def test_func(self):

        task = self.get_object()

        return self.request.user == task.owner


# удаление задачи
class TaskDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView
):

    model = Task

    template_name = 'tasks/task_confirm_delete.html'

    success_url = reverse_lazy('task_list')

    # только владелец может удалить
    def test_func(self):

        task = self.get_object()

        return self.request.user == task.owner