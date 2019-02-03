from django.urls import path
from .views import index, detail, modify

urlpatterns = [
    path('', index, name='index'),
    path('<int:task_id>/', detail, name='detail'),
    path('<int:task_id>/modify/', modify, name='modify_page')
]
