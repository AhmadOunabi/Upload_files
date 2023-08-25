from django.db import models
from .validators import valid_file
# Create your models here.

class Files(models.Model):
    name=models.CharField(max_length=20)
    file=models.FileField(upload_to='files', validators=[valid_file])
    image=models.ImageField(upload_to='images')
    
    def __str__(self) :
        return str(self.name)
