from django.urls import path
from . import views

app_name = 'pnavi'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('<int:task_id>/modify/', views.modify_page, name='modify_page'),
    path('<int:task_id>/modify_action/', views.modify_action, name='modify')
]
