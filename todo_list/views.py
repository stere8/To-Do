from django.shortcuts import render
from .models import task
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
import datetime
from django.utils import timezone

# Create your views here.


class Alltasks(ListView):
    model = task
    template_name = 'home.html'


class specifictask(DetailView):
    model = task
    template_name = 'description.html'


def finish(request,pk):
    task_at_hand = task.objects.get(id=pk)
    task_at_hand.done = True
    task_at_hand.save()
    return HttpResponseRedirect('/')


def delete(request,pk):
    task_at_hand = task.objects.get(id=pk)
    task_at_hand.delete()
    return HttpResponseRedirect('/')


def add(request):
    due_date = request.POST['date']
    name = request.POST['name']
    description = request.POST['description']
    new_task = task(name=name,due_date=due_date,description=description)
    new_task.save()
    return HttpResponseRedirect('/')