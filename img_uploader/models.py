from os import path
from pathlib import Path

import hashlib
from functools import partial

from django.db import models
from django.core.files.storage import FileSystemStorage


def hash_file(file, block_size=65536):
    hasher = hashlib.md5()
    # for buf in iter(partial(file.read, block_size), b''):
    #     hasher.update(buf)
    for chunk in file.chunks():
        hasher.update(chunk)

    return hasher.hexdigest()


# Create your models here.
def md5_filename(instance, filename):
    """
    :type instance: Image.img
    """
    filename_base, filename_ext = path.splitext(filename)

    # return path.join(instance.fs.location, "{0}{1}".format(instance.md5hex, filename_ext))
    return "{0}{1}".format(instance.md5hex, filename_ext)


class BasicTag(models.Model):
    text = models.CharField(max_length=100)
    # images = models.ManyToManyField(Image)

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text


class Image(models.Model):
    fs = FileSystemStorage(location=path.join(Path.home(), 'Desktop', 'app_media'), base_url='/img/')
    img = models.ImageField(storage=fs, upload_to='%Y/%m/%d/', width_field='img_width', height_field='img_height')
    img_width = models.PositiveIntegerField(default=1, editable=False)
    img_height = models.PositiveIntegerField(default=1, editable=False)
    md5hex = models.CharField(max_length=40, unique=True, editable=False)
    new_date = models.DateTimeField('upload date')

    tags = models.ManyToManyField(BasicTag, blank=True)

    def __str__(self):
        return self.md5hex


class Album(models.Model):
    title = models.CharField(max_length=128, unique=True)
    images = models.ManyToManyField(
        Image,
        through='AlbumImageEntry',
        through_fields=['album', 'image']
    )

    def __str__(self):
        return self.title


class AlbumImageEntry(models.Model):
    caption = models.CharField(max_length=64, blank=True)
    remark = models.TextField(blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return ".".join([self.album, self.image])
