from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .serializers import TodosSerializers, TodoSerializers
from .models import Todo

# Create your views here.

class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(done=False)
        serializer = TodosSerializers(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TodoAPIView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializers(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)
