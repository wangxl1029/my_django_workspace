from django.db import models


# Create your models here.
class BasicTag(models.Model):
    text = models.CharField(max_length=100)


class Image(models.Model):
    img = models.ImageField(upload_to='img')
    tag = models.ForeignKey(BasicTag, on_delete=models.CASCADE)
