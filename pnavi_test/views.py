from django.shortcuts import render
from django.http import HttpResponse

from .models import TestTask


# Create your views here.
def index(request):
    latest_task_list = TestTask.objects.order_by('-pub_date')[:5]
    context = {
        'latest_task_list': latest_task_list,
    }
    return render(request, 'pnavi_test/index.html', context)


def detail(request, task_id):
    return HttpResponse('This is the test task %d' % task_id)
