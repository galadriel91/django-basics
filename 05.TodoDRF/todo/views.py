from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
# Create your views here.
from .models import Todo
from .serializers import TodosSerializer, TodoSerializer

class TodosAPIView(APIView):
    def get(response, self):
        todos = Todo.objects.all()
        serializer = TodosSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TodoAPIView(APIView):
    def get(response, self, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)    