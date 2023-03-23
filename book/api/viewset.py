from rest_framework.viewsets import ModelViewSet

from book.models import Book
from book.api.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
