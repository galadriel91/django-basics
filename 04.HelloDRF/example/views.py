from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializers

# Create your views here.

class BooksApi(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializers(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)    
    

class BookApi(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializers(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
# @api_view(['GET', 'POST'])
# def BooksApi(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializers(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def BookApi(request, bid):
#     book = get_object_or_404(Book, bid=bid)
#     serializer = BookSerializers(book)
#     return Response(serializer.data, status=status.HTTP_200_OK)