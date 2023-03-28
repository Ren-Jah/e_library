from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from reader.models import Reader
from book.models import Book


class ReaderSerializer(serializers.ModelSerializer):

    def validate(self, data):
        self.__validate_phone_number(data.get('phone_num'))
        print('validating', dict(data))
        return super().validate(data)

    @staticmethod
    def __validate_phone_number(number: str):
        if not number.startswith('+7'):
            raise ValidationError('Invalid phone number.'
                             ' Phone number should start witt +7')
        if len(number[1:]) != 11:
            raise ValidationError('Invalid phone number. '
                             'Phone number should contain 11 number')

    # @staticmethod
    # def __books_in_stock(quantity_in: int):
    #     if quantity_in is None:
    #         raise ValidationError('No books in stock')

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