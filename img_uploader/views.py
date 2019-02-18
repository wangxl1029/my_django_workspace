from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import Image, hash_file, BasicTag
from .forms import UploaderForm, ImageTagEditForm


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

            return HttpResponseRedirect(reverse('img_uploader:md5img', args=(md5code,)))

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
    images = Image.objects.all()
    content = {
        'imgs': images,
    }
    # for i in imgs:
    #     print(i.img.url)
    return render(request, 'img_uploader/showing.html', content)


def show_md5(request, md5hex):
    images = Image.objects.filter(md5hex=md5hex)
    if images:
        return render(request, 'img_uploader/showing.html', {'imgs': images})

    return HttpResponse("target image md5 \"%s\" not found!" % md5hex)


@csrf_exempt
def tag_edit(request, md5hex):
    if request.method == 'POST':
        form = ImageTagEditForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            return HttpResponseRedirect(reverse('img_uploader:md5img', args=(md5hex,)))

    else:
        if BasicTag.objects.count() == 0:
            return HttpResponse('No tags available!')

        form = ImageTagEditForm()

    return render(request, 'img_uploader/tagedit.html', {'md5hex': md5hex, 'form': form})
