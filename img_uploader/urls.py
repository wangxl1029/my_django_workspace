from django.urls import path

from . import views

app_name = 'img_uploader'

urlpatterns = [
    path('', views.upload_page, name='upload_page'),
    path('upload/', views.upload, name='upload'),
    path('result/', views.show_img, name='result')
]
