from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializers

# Create your views here.

class BooksAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serialzer = BookSerializers(books, many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)
    
class BookAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, bid = pk)
        serialzer = BookSerializers(book)
        return Response(serialzer.data, status=status.HTTP_200_OK)
