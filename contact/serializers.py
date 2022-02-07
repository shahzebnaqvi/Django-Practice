from rest_framework import serializers
from contact.models import Signup, Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

class TodoUserSignup(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields= "__all__"