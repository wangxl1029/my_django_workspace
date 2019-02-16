from django.urls import path

from . import views

app_name = 'img_uploader'

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('', views.show_img, name='result')
]
