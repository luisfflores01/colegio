from django.core.exceptions import ValidationError


def validar_celular(value):
    if value < 0:
        raise ValidationError(
            '%(value)s el número de celular debe ser positivo',
            params={'value': value},
        )
    # if value > 9:
    #     raise ValidationError(
    #         '%(value)s el número de celular debe contener ocho digitos',
    #         params={'value': value},
    #     )
