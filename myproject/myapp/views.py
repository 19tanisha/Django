from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo
# Create your views here.

def index(request):
    return HttpResponse('hello world')

def add(request):
    task = ToDo.objects.all()
    context = {
        'task':task
    }
    return render(request,'myapp/add.html', context)