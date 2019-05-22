from django.shortcuts import render, redirect, render_to_response
from .forms import LoginFrom, SignUp
from jsonschema.exceptions import ValidationError
from django.contrib.auth import login, authenticate, logout

def home(request):
    return render(request, "home.html")


def conocenos(request):
    return render(request, "observatorio/conocenos.html")


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            usernm = request.POST['username']
            passwrd = request.POST['password']
            user = authenticate(request, username=usernm, password=passwrd)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('/home')
            else:
                form = LoginFrom()
                args = {'form': form}
                return render(request, 'observatorio/login.html', args)
        else:
            form = LoginFrom()
            args = {'form': form}
            return render(request, 'observatorio/login.html', args)
    else:
        return redirect('/admin/')


def signup(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUp()
    return render(request, 'observatorio/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/home')
