from django import forms
from .models import Files
class FileUploadForm(forms.ModelForm):
    class Meta:
        model= Files
        fields=['name','file','image']
        
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'file':forms.FileInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
        }
