from django.shortcuts import render

from .models import TestTask


# Create your views here.
def index(request):
    latest_task_list = TestTask.objects.order_by('-pub_date')[:5]
    context = {
        'latest_task_list': latest_task_list,
    }
    return render(request, 'pnavi_test/index.html', context)


def detail(request, task_id):
    task = TestTask.objects.get(pk=task_id)
    context = {
        'test_title': task.test_title,
        'test_items': task.testitem_set.all()
    }
    return render(request, 'pnavi_test/detail.html', context)
