from rest_framework import serializers
from .models import Todo

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id', 'title', 'important', 'done'
        )

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id', 'title', 'content', 'created', 'important', 'done'
        )


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'title', 'content', 'important'
        )