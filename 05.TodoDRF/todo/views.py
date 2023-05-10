from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
# Create your views here.
from .models import Todo
from .serializers import TodosSerializer, TodoSerializer, CreateSerializer

class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodosSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = CreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
class TodoAPIView(APIView):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    def put(self, request, pk):
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class DoneAPIView(APIView):
    def get(self, request):
        dones = Todo.objects.filter(done=True)
        serializer = TodosSerializer(dones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  

class DoneEditAPIView(APIView):
    def get(self, request, pk):
        done = get_object_or_404(Todo, id=pk)
        done.done = True
        done.save()
        TodoSerializer(done)
        return Response(status=status.HTTP_200_OK)      