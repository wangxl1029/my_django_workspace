from django.urls import path
from .views import index, detail

urlpatterns = [
    path('', index, name='pnavi'),
    path('<int:task_id>/', detail, name='detail')
]
