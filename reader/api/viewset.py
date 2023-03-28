from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from reader.models import Reader
from reader.api.serializers import ReaderSerializer


class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = ['is_active']
