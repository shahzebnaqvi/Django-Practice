from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the contact index.")

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from contact.serializers import TodoSerializer, TodocustomerUsers
from contact.models import  Todo, customerUsers

# Create your views here.
class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# user signup view api
class ListcustomerUsersAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = customerUsers.objects.all()
    serializer_class = TodocustomerUsers

class CreatecustomerUsersAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = customerUsers.objects.all()
    serializer_class = TodocustomerUsers

class UpdatecustomerUsersAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = customerUsers.objects.all()
    serializer_class = TodocustomerUsers

class DeletecustomerUsersAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = customerUsers.objects.all()
    serializer_class = TodocustomerUsers