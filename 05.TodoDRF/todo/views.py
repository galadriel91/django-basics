from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .models import Todo
from .serializers import TodosSerializer

class TodosAPIView(APIView):
    def get(response, self):
        todos = Todo.objects.all()
        serializer = TodosSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)