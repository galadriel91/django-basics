from rest_framework import serializers
from .models import Todo

class TodosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id', 'title', 'important', 'done'
        )

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            'id', 'title', 'content', 'important', 'created', 'done'
        )        