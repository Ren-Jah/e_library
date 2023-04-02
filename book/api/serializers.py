from rest_framework import serializers

from book.models import Book


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "pages_amount",
            "author",
            "quantity_in",
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "pages_amount",
            "author",
            "quantity_in",
        ]