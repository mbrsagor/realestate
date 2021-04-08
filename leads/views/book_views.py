from leads.models.book import Book
from leads.serializers.book_serializer import BookSerializer
from rest_framework import permissions, viewsets


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[permissions.AllowAny]
    