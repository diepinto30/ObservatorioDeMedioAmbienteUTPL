from django.shortcuts import render, redirect, render_to_response
from .forms import LoginFrom, SignUp, ContenidoFrom
from django.contrib.auth import login, authenticate, logout
from .models import GestorContenidos


def home(request):
    contenido = GestorContenidos.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo}
    return render(request, "home.html", dic)


def conocenos(request):
    contenido = GestorContenidos.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/conocenos.html", dic)


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            usernm = request.POST['username']
            passwrd = request.POST['password']
            user = authenticate(request, username=usernm, password=passwrd)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('/')
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
    return redirect('/')


def GestorContenido(request):
    if request.method == 'POST':
        form = ContenidoFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = ContenidoFrom()
    return render(request, 'observatorio/GestorContenido.html', {'form': form})


def Contenido_edit(request, id):
    Contenido = GestorContenidos.objects.get(idGestorContenidos=id)
    if request.method == 'GET':
        form = ContenidoFrom(instance=Contenido)
    else:
        form = ContenidoFrom(request.POST, instance=Contenido)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'observatorio/EditorDeContenido.html', {'form': form})


def EliminarContenido(request, id):
    Contenido = GestorContenidos.objects.get(idGestorContenidos=id)
    if request.method == 'POST':
        Contenido.delete()
        return redirect('/')
    return render(request, 'observatorio/EliminarContenido.html', {'Contenido': Contenido})
