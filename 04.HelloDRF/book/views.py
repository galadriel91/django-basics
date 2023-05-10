from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializers
# Create your views here.

class BooksAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializers(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)