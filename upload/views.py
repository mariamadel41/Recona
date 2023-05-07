from django.shortcuts import render

# Create your views here.
from .forms import UploadForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'upload/success.html')
    else:
        form = UploadForm()
    return render(request, 'upload/upload.html', {'form': form})
