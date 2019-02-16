from django.urls import path, re_path

from . import views

app_name = 'img_uploader'

urlpatterns = [
    path('', views.show_img, name='result'),
    path('upload', views.upload, name='upload'),
    re_path(r'(?P<md5hex>[0-9a-f]{32})$', views.show_md5, name='md5img')
]
