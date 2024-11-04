from django.urls import path
from . import views # . means import from the same directory

urlpatterns = [
    #load page of the app will be sent to the 'index.html' file
    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='add'),

    # add a path of the completed items in our list to our database
    path('completed/<todo_id>', views.completedTodo, name = 'completed')
]