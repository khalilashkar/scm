import  os 
from django.core.exceptions import ValidationError
def validate_file_extensison(value):
    ext=os.path.splitext(value.name)[1]
    valid_extension=['.pdf','.doc']
    if not ext.lower() in valid_extension:
        raise ValidationError('unsported file extension ')