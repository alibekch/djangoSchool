from django.forms import ValidationError
from datetime import date, datetime
from datetime import timedelta


def validate_phone_number(phone:str):
    phone = phone.replace(' ', '')

    if len(phone)  !=12:
        raise ValidationError('Длина номера не совпадает')
    
    if not phone.startswith('+7'):
        raise ValidationError('wrong number format')
    
    digits = '+0123456789'

    for i in phone:
        if i not in digits:
            raise ValidationError('only digits')