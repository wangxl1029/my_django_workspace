from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('This is predictive navigation page.')


def detail(request, task_id):
    return HttpResponse('This is the test task %d' % task_id)
