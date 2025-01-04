from django.urls import path
from .views import home, task_list, create_task, delete_task, update_task
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('task_list/', task_list, name='task_list'),
    path('home/', home, name='home'),
    path('create/', create_task, name='create_task'),
    path('<int:task_id>/delete/', delete_task, name='delete_task'),
    path('<int:task_id>/update/', update_task, name='update_task'),
    # Add more URL patterns for creating, updating, deleting tasks, etc.
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)