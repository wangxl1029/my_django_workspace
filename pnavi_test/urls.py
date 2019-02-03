from django.urls import path
from .views import index, detail, modify_page, modify_action

urlpatterns = [
    path('', index, name='index'),
    path('<int:task_id>/', detail, name='detail'),
    path('<int:task_id>/modify/', modify_page, name='modify_page'),
    path('<int:task_id>/modify_action/', modify_action, name='modify')
]
