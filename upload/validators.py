from django.core.exceptions import ValidationError

def valid_file(value):
    if value.size > 10485760:
        raise ValidationError('Only Files with maxsize 10Mb are allowed')
    else:
        value=str(value)
        if value.endswith('.pdf') != True and value.endswith('.txt') != True and value.endswith('.doc') != True:
            raise ValidationError('Only PDF, DOC and TXT files are allowed')
        else:
            return value