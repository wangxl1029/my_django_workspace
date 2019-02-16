from django.urls import path

from . import views

app_name = 'img_uploader'

urlpatterns = [
    # path('upload', views.upload_page, name='upload_page'),
    # path('upload_action/', views.upload, name='upload'),
    path('upload', views.upload, name='upload'),
    path('', views.show_img, name='result')
]
