from django.shortcuts import render
from .models import Image


# Create your views here.
def uploadImg(request):
    """
    图片上传
    :param request:
    :return:
    """
    if request.method == 'POST':
        new_img = Image(
            img=request.FILES.get('img'),
            name=request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'img_uploader/uploading.html')

