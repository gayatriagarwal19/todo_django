from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    todos = Task.objects.all()

    if request.method=='POST':
        form= TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form= TaskForm()

    context= {
        'todos' : todos,
        'form' : form,
    }

    return render(request, 'todo/index.html' , context)

def delete(request, pk):
    todo= Task.objects.get(id=pk)
    if request.method=='POST':
        todo.delete()
        return redirect('/')
    return render(request, 'todo/delete.html')    

