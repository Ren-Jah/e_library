from rest_framework.viewsets import ModelViewSet

from reader.models import Reader
from reader.api.serializers import ReaderSerializer


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
