from django.shortcuts import render ,redirect
from .models import Files
from .forms import FileUploadForm
# Create your views here.

def file_upload(request):
    if request.method == 'POST':
        form=FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('----------------------------NO----------------------------')
    else:
        form=FileUploadForm()
    return render(request, 'upload.html',{'form':form})
