from rest_framework import views, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .serializers import TodoSerializers, TodosSerializers
from .models import Todo

# Create your views here.
class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodosSerializers(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = TodosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoAPIView(APIView):
    def get(self, request, id):
        todo = get_object_or_404(Todo, id=id)
        serializer = TodoSerializers(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)