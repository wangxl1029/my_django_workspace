from django.urls import path, register_converter

from . import views, converters


register_converter(converters.MD5hex32Converter, 'md5hex')

app_name = 'img_uploader'

urlpatterns = [
    path('', views.show_img, name='result'),
    path('upload', views.upload, name='upload'),
    path('<md5hex:md5hex>/', views.show_md5, name='md5img'),
    path('<md5hex:md5hex>/tagedit/', views.tag_edit, name='tag_edit')
]
