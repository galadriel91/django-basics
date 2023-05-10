from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Book
from .serializers import BookSerializers
# Create your views here.

class BooksAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializers(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BookAPIView(APIView):
    def get(self, request, pk):
        books = get_object_or_404(Book, bid = pk)
        serializer = BookSerializers(books)
        return Response(serializer.data, status=status.HTTP_200_OK)
