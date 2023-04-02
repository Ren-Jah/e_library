from author.models import Author
from author.api.serializers import AuthorSerializer, AuthorCreateSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from author.api.permissions import IsAdmin


class AuthorCreateView(CreateAPIView):
    """ Вьюшка для создания авторов """
    model = Author
    permission_classes = [IsAdmin]
    serializer_class = AuthorCreateSerializer


class AuthorListView(ListAPIView):
    """ Вьюшка для выведения списка авторов """
    model = Author
    permission_classes = [AllowAny]
    serializer_class = AuthorSerializer

    def get_queryset(self):
        """ Метод для выведения списка авторов """
        return Author.objects.all()


class AuthorView(RetrieveUpdateDestroyAPIView):
    """ Вьюшка для взаимодействия с информацией об авторах """
    queryset = Author.objects.all()
    model = Author
    permission_classes = [IsAdmin]
    serializer_class = AuthorSerializer
    lookup_field = 'pk'


