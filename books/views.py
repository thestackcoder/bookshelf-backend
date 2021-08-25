from django.shortcuts import render
from rest_framework import viewsets , serializers
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

class BookViewSet(viewsets.ModelViewSet):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['POST'])
def searchBook(request):
    if request.method == 'POST':
        searchStr = request.data['search_string']
        try:
            result = Book.objects.all()
        except Book.DoesNotExist:
            result = None
        # print(go)
        if result is not None:
            user_books = Book.objects.filter( title__contains = searchStr) | Book.objects.filter( author__first_name__contains=searchStr) | Book.objects.filter( author__last_name__contains=searchStr) | Book.objects.filter( topic__name__contains=searchStr) | Book.objects.filter( storage__name__contains=searchStr) | Book.objects.filter( storage__storage_type__contains=searchStr)
            serializer = BookSerializer(user_books, many=True)
            return JsonResponse(serializer.data, safe=False)
            
        else:
            return Response({"message": "Book does not exist " , "status": status.HTTP_409_CONFLICT})
        
        
    
    else:
        return Response({"detail": "Invalid Request!",  "status": status.HTTP_400_BAD_REQUEST})
