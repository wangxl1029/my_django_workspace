from django.db import models


# Create your models here.
class Image(models.Model):
    # tag = models.ForeignKey(BasicTag, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)
    new_date = models.DateTimeField('upload date')


class BasicTag(models.Model):
    text = models.CharField(max_length=100)

