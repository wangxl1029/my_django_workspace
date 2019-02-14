from os import path
from pathlib import Path

import hashlib
from functools import partial

from django.db import models
from django.core.files.storage import FileSystemStorage


def hash_file(file, block_size=65536):
    hasher = hashlib.md5()
    for buf in iter(partial(file.read, block_size), b''):
        hasher.update(buf)

    return hasher.hexdigest()


# Create your models here.
def md5_filename(instance, filename):
    """
    :type instance: Image.img
    """
    filename_base, filename_ext = path.splitext(filename)

    # return path.join(instance.fs.location, "{0}{1}".format(instance.md5hex, filename_ext))
    return "{0}{1}".format(instance.md5hex, filename_ext)


class Image(models.Model):
    fs = FileSystemStorage(location=path.join(Path.home(), 'Desktop', 'app_media'), base_url='/img/')
    # tag = models.ForeignKey(BasicTag, on_delete=models.CASCADE)
    img = models.ImageField(storage=fs, upload_to='%Y/%m/%d/', width_field='img_width', height_field='img_height')
    img_width = models.PositiveIntegerField(default=1)
    img_height = models.PositiveIntegerField(default=1)
    md5hex = models.CharField(max_length=40, unique=True)
    new_date = models.DateTimeField('upload date')


class BasicTag(models.Model):
    text = models.CharField(max_length=100)

