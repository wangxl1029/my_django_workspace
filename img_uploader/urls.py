from django.urls import path

from . import views

app_name = 'img_uploader'

urlpatterns = [
    path('', views.uploadImg, name='upload')
]
