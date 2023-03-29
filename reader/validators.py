from rest_framework.exceptions import ValidationError


def validate_phone_num(number: str):
    if not number.startswith('+7'):
        raise ValidationError('Phone number should start with +7')
    if len(number[1:]) != 11:
        raise ValidationError('Phone number should contain 11 number')