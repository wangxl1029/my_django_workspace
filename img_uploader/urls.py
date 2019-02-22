from django.urls import path, register_converter

from . import views, converters


register_converter(converters.MD5hex32Converter, 'md5hex')

app_name = 'img_uploader'

urlpatterns = [
    path('', views.show_img, name='result'),
    path('upload', views.upload, name='upload'),
    path('albums/', views.AlbumListView.as_view(), name='album_list'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('albums/<int:album_id>/', views.album_at, name='album_at'),
    path('albums_entry_edit/<int:entry_id>/', views.album_entry_edit, name='album_entry_edit'),
    path('<md5hex:md5hex>/', views.show_md5, name='md5img'),
    path('<md5hex:md5hex>/tag_edit/', views.tag_edit, name='tag_edit'), path('<md5hex:md5hex>/te/', views.tag_edit),
    path('<md5hex:md5hex>/add_to_album/', views.add_image_to_album, name='add_img2album'),
    path('<md5hex:md5hex>/a2a', views.add_image_to_album)
]
