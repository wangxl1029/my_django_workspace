from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages

from .models import Image, hash_file, BasicTag, Album, AlbumImageEntry
from .forms import UploaderForm, ImageTagEditForm, EditEntryInAlbumForm


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
            req_img = form.cleaned_data['img']
            print(req_img)
            md5hex = hash_file(req_img)
            print('md5 {0} from request'.format(md5hex))

            try:
                Image.objects.get(md5hex=md5hex)
                messages.warning(request, "Duplicated uploading image \"%s\"!" % md5hex)
            except Image.DoesNotExist:
                new_img = form.save(commit=False)
                new_img.md5hex = md5hex
                new_img.new_date = timezone.now()
                new_img.save()
                form.save_m2m()
                messages.info(request, "New image \"%s\" uploaded OK." % md5hex)

            return HttpResponseRedirect(reverse('img_uploader:md5img', args=(md5hex,)))

    else:
        form = UploaderForm()

    return render(request, 'img_uploader/uploading.html', {'form': form})


def show_img(request):
    """
    图片显示
    :param request:
    :return:
    """
    images = Image.objects.all().order_by('-new_date')
    content = {
        'imgs': images,
    }
    return render(request, 'img_uploader/showing.html', content)


def show_md5(request, md5hex):
    images = Image.objects.filter(md5hex=md5hex)
    if images:
        return render(request, 'img_uploader/showing.html', {'imgs': images})

    return HttpResponse("target image md5 \"%s\" not found!" % md5hex)


def tag_edit(request, md5hex):
    image = get_object_or_404(Image, md5hex=md5hex)
    if request.method == 'POST':
        form = ImageTagEditForm(request.POST, instance=image)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

            messages.info(request, "The tag of image \"%s\" is updated ok." % md5hex)
            return HttpResponseRedirect(reverse('img_uploader:md5img', args=(md5hex,)))

        else:
            print(request.POST)
    else:
        if BasicTag.objects.count() == 0:
            return HttpResponse('No tags available!')

        form = ImageTagEditForm(instance=image)

    return render(request, 'img_uploader/tagedit.html', {'md5hex': md5hex, 'form': form})


def add_image_to_album(request, md5hex):
    image = get_object_or_404(Image, md5hex=md5hex)
    if request.method == 'POST':
        try:
            album_selected = request.POST['album_entry']
        except KeyError:
            messages.info(request, "No album selected!")
            return HttpResponseRedirect(reverse('img_uploader:md5img', args=(md5hex,)))
        else:
            album_target = get_object_or_404(Album, pk=album_selected)
            AlbumImageEntry.objects.create(image=image, album=album_target)

            return HttpResponseRedirect(reverse('img_uploader:album_at', args=(album_selected,)))

    else:
        to_list = Album.objects.exclude(id__in=[a.id for a in image.albums.all()])
        return render(request, 'img_uploader/albumedit.html', {'img': image, 'to_list': to_list})


def album_index(request):
    return HttpResponse("album index page")


def album_at(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'img_uploader/album.html', {'album': album})


def album_entry_edit(request, entry_id):
    image_entry = get_object_or_404(AlbumImageEntry, pk=entry_id)
    has_contents = image_entry.caption or image_entry.remark
    if request.method == 'POST':
        try:
            operation = request.POST['operation']
        except KeyError:
            operation = 'edit'
        else:
            if "remove" == operation:
                image_entry.delete()

        if "edit" == operation:
            form = EditEntryInAlbumForm(request.POST, instance=image_entry)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('img_uploader:album_at', args=(image_entry.album.id,)))

        return HttpResponseRedirect(reverse('img_uploader:md5img', args=(image_entry.image.md5hex,)))

    else:
        form = EditEntryInAlbumForm(instance=image_entry)

    return render(request, 'img_uploader/album_entry_edit.html',
                  {'entry': image_entry, 'is_allow_remove': not has_contents, 'form': form})
