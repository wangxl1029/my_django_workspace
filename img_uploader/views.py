from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Image


# Create your views here.
def upload(request):
    """
    图片上传
    :param request:
    :return:
    """
    if request.method == 'POST':
        new_img = Image(
            img=request.FILES.get('img'),
            name=request.FILES.get('img').name,
            new_date=timezone.now()
        )
        new_img.save()
        return HttpResponseRedirect(reverse('img_uploader:result'))


def upload_page(request):
    return render(request, 'img_uploader/uploading.html')


def show_img(request):
    """
    图片显示
    :param request:
    :return:
    """
    imgs = Image.objects.all()
    content = {
        'imgs': imgs,
    }
    for i in imgs:
        print(i.img.url)
    return render(request, 'img_uploader/showing.html', content)

