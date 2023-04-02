from reader.models import Reader
from reader.api.serializers import ReaderCreateSerializer, ReaderSerializer, ReaderListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import AllowAny
from author.api.permissions import IsAdmin, IsOwner


class ReaderCreateView(CreateAPIView):
    """ Вьюшка для создания нового читателя """
    model = Reader
    serializer_class = ReaderCreateSerializer


class ReaderListView(ListAPIView):
    """ Вьюшка для выведения списка читателей """
    model = Reader
    serializer_class = ReaderListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """ Метод для возврата всех читателей """
        return Reader.objects.all()


class ReaderView(RetrieveUpdateDestroyAPIView):
    """ Вьюшка для взаимодействия с информацией о читателях """
    queryset = Reader.objects.all()
    model = Reader
    serializer_class = ReaderSerializer
    permission_classes = [IsOwner | IsAdmin]
    lookup_field = 'pk'

