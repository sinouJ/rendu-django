from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index_view(request):
    return render(request, 'home/home.html')

def user_login(request):

    if(request.method == 'POST'):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index_view')
        
        else:
            return 'TODO error log message'

    else: 
        form = AuthenticationForm()

    return render(request, 'home/login.html', {'form': form})

def user_signup(request):
    page_title = 'Inscription'

    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)

        if(form.is_valid()):
            form.save()
    else:
        form = UserCreationForm()

    return render(request, 'home/signup.html', {'form': form})

def user_logout(request):
    logout(request)

    return redirect('index_view')