from django.shortcuts import render

def projets_view(request):
    return render(request, 'nos_projets/index.html')
