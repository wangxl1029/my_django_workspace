from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TestTask


# Create your views here.
def index(request):
    latest_task_list = TestTask.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_task_list': latest_task_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, task_id):
    return HttpResponse('This is the test task %d' % task_id)
