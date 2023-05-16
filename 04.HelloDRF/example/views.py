from rest_framework import views, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializers
# Create your views here.

class BooksView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializers(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BookView(APIView):
    def get(self, request , pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializers(book)
        return Response(serializer.data, status=status.HTTP_200_OK)    