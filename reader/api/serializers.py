from rest_framework import serializers
from reader.models import Reader



class ReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reader
        fields = [
            "id",
            "name",
            "surname",
            "phone_num",
            "is_active",
            "active_books",
        ]