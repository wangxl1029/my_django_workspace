from os import path
import hashlib
from functools import partial

from django.db import models


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
    instance.img.open()
    filename_base, filename_ext = path.splitext(filename)

    return "{0}{1}".format(hash_file(instance.img), filename_ext)


class Image(models.Model):
    # tag = models.ForeignKey(BasicTag, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=md5_filename, width_field='img_width', height_field='img_height')
    img_width = models.PositiveIntegerField(default=1)
    img_height = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=20)
    new_date = models.DateTimeField('upload date')


class BasicTag(models.Model):
    text = models.CharField(max_length=100)

