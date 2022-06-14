from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer

#+api view
from rest_framework.decorators import api_view
from rest_framework.response import Response
#-status
from rest_framework import status

# Create your views here.
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>'
    )




# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world!"})

# @api_view(['GET'])
# def todo_list(request):
#     queryset = Todo.objects.all()
#     TodoSerializers = TodoSerializer(queryset, many=True)
#     return Response(TodoSerializers.data)

# @api_view(["POST"])
# def create_todo(request):
#     serializer = TodoSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)



# @api_view(['PUT','GET'])
# def todo_update(request,pk):
#     todo = Todo.objects.get(id=pk)
#     if request.method == 'GET':
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = TodoSerializer(instance=todo,data=request.data)#? gelen veriyle putdan gelen veriyi karşılatır güncelle
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_UPDATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def todo_delete(request,pk):
#     todo = Todo.objects.get(id=pk)
#     todo.delete()
#     return Response("item deleted",status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def todo_list_create(request):
    if request.method == 'GET':
        queryset = Todo.objects.all()
        TodoSerializers = TodoSerializer(queryset, many=True)
        return Response(TodoSerializers.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def todoUpdate(request, pk):
    
    querset =  Todo.objects.get(id = pk)
    
    if request.method == "GET":
        serializer = TodoSerializer(querset)
    
        return Response(serializer.data)
        
    elif request.method == "PUT":
        
        serializer = TodoSerializer(instance=querset,  data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "DELETE":
      
        querset.delete()
        return Response("Item Deleted")
        