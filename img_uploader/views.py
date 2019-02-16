from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import IntegrityError

from .models import Image, hash_file
from .forms import UploaderForm


# Create your views here.
def upload(request):
    """
    图片上传
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = UploaderForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['img']

            img.open()
            md5code = hash_file(img)
            print('md5 {0} from request'.format(md5code))

            try:
                Image.objects.get(md5hex=md5code)
            except Image.DoesNotExist:
                new_img = Image(
                    img=img,
                    md5hex=md5code,
                    new_date=timezone.now()
                )

                try:
                    print(new_img.md5hex)
                    new_img.save()
                except IntegrityError:
                    return HttpResponse("I figure you pick a non-picture!")

            return HttpResponseRedirect(reverse('img_uploader:result'))

    else:
        form = UploaderForm()

    return render(request, 'img_uploader/uploading.html', {'form': form})


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

