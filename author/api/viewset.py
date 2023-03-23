from rest_framework.viewsets import ModelViewSet

from author.models import Author
from author.api.serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer