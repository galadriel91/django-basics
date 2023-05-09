from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodosSerializers
from .models import Todo

# Create your views here.

class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(done=False)
        serializer = TodosSerializers(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
