from rest_framework import views, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .serializers import TodoSerializers
from .models import Todo

# Create your views here.
class TodosAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

class TodoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
    lookup_field = 'id'
    
class TodoDoneAPIView(generics.ListAPIView):
    queryset = Todo.objects.filter(done=True)
    serializer_class = TodoSerializers

class TodoDoneCheckAPIView(APIView):
    def get(self, request, id):
        done = get_object_or_404(Todo, id=id) 
        done.done = True
        done.save()
        serializer = TodoSerializers(done)
        return Response(status=status.HTTP_200_OK)    