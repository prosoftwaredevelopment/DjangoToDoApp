from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def submit(request):
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.save()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

def delete(request,id):
    obj = Todo.objects.get(id=id)
    obj.delete()
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)

def list(request):
    mydictionary = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list.html',context=mydictionary)
