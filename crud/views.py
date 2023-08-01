from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book_details
from .serializers import BookSerializer

@api_view(['POST', 'PUT', 'DELETE','GET'])
def Book_view(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Book Added", "data": serializer.data})
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        book_id = request.data.get('Book_id')
        try:
            book = Book_details.objects.get(Book_id=book_id)
        except Book_details.DoesNotExist:
            return Response({"message": "Book not found"}, status=404)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Book name updated", "data": serializer.data})
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        book_id = request.data.get('Book_id')
        try:
            book = Book_details.objects.get(Book_id=book_id)
            book.delete()
            return Response({"message": "Book deleted successfully"})
        except Book_details.DoesNotExist:
            return Response({"message": "Book not found"}, status=404)
        

    elif request.method == 'GET':
        
        books = Book_details.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    return Response({"message": "Hello, World!"})
