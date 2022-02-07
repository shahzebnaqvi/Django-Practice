from rest_framework import serializers
from contact.models import  Todo, customerUsers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

class TodocustomerUsers(serializers.ModelSerializer):
    class Meta:
        model = customerUsers
        fields= "__all__"