from rest_framework import serializers
from reader.models import Reader


class ReaderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = [
            "id",
            "username",
            "password",
            "name",
            "surname",
            "phone_num",
        ]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user


class ReaderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = [
            "id",
            "name",
            "surname",
            "active_books",
        ]


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