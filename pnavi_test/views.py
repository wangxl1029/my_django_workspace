from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import TestTask


# Create your views here.
def index(request):
    latest_task_list = TestTask.objects.order_by('-pub_date')[:5]
    context = {
        'latest_task_list': latest_task_list,
    }
    return render(request, 'pnavi_test/index.html', context)


def detail(request, task_id):
    task = get_object_or_404(TestTask, pk=task_id)
    return render(request, 'pnavi_test/detail.html', {'test_task': task, })


def modify_page(request, task_id):
    task = get_object_or_404(TestTask, pk=task_id)
    return render(request, 'pnavi_test/modify.html', {'test_task': task, })


def modify_action(request, task_id):
    return HttpResponseRedirect(reverse('detail', args=(task_id,)))
