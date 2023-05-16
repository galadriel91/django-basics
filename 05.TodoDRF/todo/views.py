from rest_framework import views, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializers
from .models import Todo

# Create your views here.
class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializers(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
