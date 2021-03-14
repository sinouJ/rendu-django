from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PostCVForm

def candidature_view(request):
    if request.method == 'POST':
        form = PostCVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = PostCVForm()
    return render(request, 'candidature/home.html', {'form': form})

def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
        else:
            form = ModelFormWithFileField()
        return render(request, 'upload.html', {'form': form})
