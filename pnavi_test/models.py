from django.db import models


# Create your models here.
class TestTask(models.Model):
    test_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.test_title


class TestItem(models.Model):
    task = models.ForeignKey(TestTask, on_delete=models.CASCADE)
    item_text = models.CharField(max_length=200)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text
