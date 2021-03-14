from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostCVForm
from .models import PostCV
from django.utils import timezone

def candidature_view(request):
    candidatures = PostCV.objects.all()
    return render(request, 'candidature/home.html', {'candidatures': candidatures})

def post_cv_view(request):
    if request.method == 'POST':
        form = PostCVForm(request.POST, request.FILES)

        if form.is_valid():
            cv = form.save(commit = False)
            cv.author = request.user
            cv.published_date = timezone.now()
            cv.fileCV = request.FILES['fileCV']
            form.save()
            return redirect('candidature_view')
        
        else: 
            return render(request, 'candidature/home.html')

    else:
        form = PostCVForm()
    return render(request, 'candidature/post_cv.html', {'form': form})

def detail_candidature_view(request, id):
    candidature = get_object_or_404(PostCV, id = id)
    return render(request, 'candidature/detail_candidature_view.html', {'candidature': candidature})