from book.models import Book
from book.api.serializers import BookSerializer, BookCreateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from author.api.permissions import IsAdmin


class BookCreateView(CreateAPIView):
    """ Вьюшка для создания книг """
    model = Book
    permission_classes = [IsAdmin]
    serializer_class = BookCreateSerializer


class BookListView(ListAPIView):
    """ Вьюшка для выведения списка книг """
    model = Book
    permission_classes = [AllowAny]
    serializer_class = BookSerializer

    def get_queryset(self):
        """ Метод для выведения всех книг """
        return Book.objects.all()


class BookView(RetrieveUpdateDestroyAPIView):
    """ Вьюшка для взаимодействия с информацией о книгах """
    queryset = Book.objects.all()
    model = Book
    permission_classes = [IsAdmin]
    serializer_class = BookSerializer
    lookup_field = 'pk'



