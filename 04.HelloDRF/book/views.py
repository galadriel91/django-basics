from rest_framework import status, viewsets, generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Book
from .serializers import BookSerializers
# Create your views here.


class BooksAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class BookAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'bid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
