from django.urls import path
# from .views import create_todo, home, todo_list, todo_update,todo_delete,
from .views import  todo_list_create,home, todoUpdate


urlpatterns = [
    path('', home),
    # path("hello",hello_world,name="hello_world"),
    # path("todos",todo_list,name="todo_list"),
    # path("addtodo",create_todo,name="create_todo"),
    path("todos",todo_list_create,name="todo_list_create"),
    # path("todos/<int:pk>",todo_list_create,name="todo_list_create"),
    path("todo/<int:pk>",todoUpdate,name="todo_list_update"),
    # path("todoupdate/<int:pk>",todo_update,name="todo_update"),
    # path("tododelete/<int:pk>",todo_delete,name="todo_delete"),
]
