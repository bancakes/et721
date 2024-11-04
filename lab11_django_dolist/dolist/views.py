from django.shortcuts import render, redirect
from .models import Todolist
from .forms import TodoListForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    todo_tasks = Todolist.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_tasks' : todo_tasks, 'form':form}
    return render(request, 'index.html', context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    print(request.POST['text']) # for testing
    # print(request.POST['text']) # testing if the app is capturing 

    #capture data from the text field after the form is submitted 
    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()

# function to mark a task 
def completedTodo(request, todo_id):
    todo = Todolist.objects.get(pk = todo_id)
    todo.completed = True
    todo.save()
    
    return redirect('index')