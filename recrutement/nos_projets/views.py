from django.shortcuts import render

def index_view(request):
    return render(request, 'nos_projets/base.html')
