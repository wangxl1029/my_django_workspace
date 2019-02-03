from django.shortcuts import render
from django.http import Http404

from .models import TestTask


# Create your views here.
def index(request):
    latest_task_list = TestTask.objects.order_by('-pub_date')[:5]
    context = {
        'latest_task_list': latest_task_list,
    }
    return render(request, 'pnavi_test/index.html', context)


def detail(request, task_id):
    try:
        task = TestTask.objects.get(pk=task_id)
    except TestTask.DoesNotExist:
        raise Http404("Test task does not exist!")
    return render(request, 'pnavi_test/detail.html', {'test_task': task, })
