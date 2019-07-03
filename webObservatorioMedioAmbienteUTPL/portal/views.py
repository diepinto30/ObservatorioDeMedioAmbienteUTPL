from django.shortcuts import render, redirect, render_to_response
from .forms import LoginFrom, SignUp, ContenidoFrom, PublicacionesFrom, ParticipantesFrom
from django.contrib.auth import login, authenticate, logout
from .models import GestorContenidos
from .models import GestorPublicaciones, GestorParticipantes


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
    return render(request, 'observatorio/GestorContenido/GestorContenido.html', {'form': form})


def Contenido_edit(request, id):
    Contenido = GestorContenidos.objects.get(idGestorContenidos=id)
    if request.method == 'GET':
        form = ContenidoFrom(instance=Contenido)
    else:
        form = ContenidoFrom(request.POST, instance=Contenido)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'observatorio/GestorContenido/EditorDeContenido.html', {'form': form})


def EliminarContenido(request, id):
    Contenido = GestorContenidos.objects.get(idGestorContenidos=id)
    if request.method == 'POST':
        Contenido.delete()
        return redirect('/')
    return render(request, 'observatorio/GestorContenido/EliminarContenido.html', {'Contenido': Contenido})


# gestor de publicaciones del sitio
def GestorPublicacion(request):
    if request.method == 'POST':
        form = PublicacionesFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = PublicacionesFrom()
    return render(request, 'observatorio/GestorContenido/GestorPublicaciones.html', {'form': form})


def Publicaciones_edit(request, id):
    Contenido = GestorPublicaciones.objects.get(idGestorPublicaciones=id)
    if request.method == 'GET':
        form = PublicacionesFrom(instance=Contenido)
    else:
        form = PublicacionesFrom(request.POST, instance=Contenido)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'observatorio/GestorContenido/EditorDePublicaciones.html', {'form': form})


def EliminarPublicaciones(request, id):
    Contenido = GestorPublicaciones.objects.get(idGestorPublicaciones=id)
    if request.method == 'POST':
        Contenido.delete()
        return redirect('/')
    return render(request, 'observatorio/GestorContenido/EliminarPublicaciones.html', {'Contenido': Contenido})


# Gestor de Participantes
def GestorParticipantess(request):
    if request.method == 'POST':
        form = ParticipantesFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = ParticipantesFrom()
    return render(request, 'observatorio/GestorContenido/GestorParticipantes.html', {'form': form})


# sitios de los contenido
def Agua_view(request):
    contenido = GestorContenidos.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/Componentes/agua.html", dic)


def MedioAmbiente_view(request):
    contenido = GestorContenidos.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/Componentes/MedioAmbiente.html", dic)


def CalidadDeVida_view(request):
    contenido = GestorContenidos.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/Componentes/CalidadDeVida.html", dic)


def Equidad_view(request):
    contenido = GestorContenidos.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/Componentes/Equidad.html", dic)


def Mercados_view(request):
    contenido = GestorContenidos.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/Componentes/Mercados.html", dic)


def ParticipacionDemocracia_view(request):
    contenido = GestorContenidos.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/Componentes/ParticipacionDemocracia.html", dic)


def Etnozoologia_view(request):
    contenido = GestorContenidos.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/Componentes/Etnozoologia.html", dic)


# sitios de las publicaciones
def RevistasIn_view(request):
    contenido = GestorPublicaciones.objects.all()
    subtitulo = ""
    dic = {'list_Publicaciones': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/Publicaciones/RevistasIndexadas.html", dic)


def Tesis_view(request):
    contenido = GestorPublicaciones.objects.all()
    subtitulo = ""
    dic = {'list_Publicaciones': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/Publicaciones/TrabajosTitulacion.html", dic)


def ArticulosDiv_view(request):
    contenido = GestorPublicaciones.objects.all()
    subtitulo = ""
    dic = {'list_Publicaciones': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/Publicaciones/ArticulosDivulgacion.html", dic)


def ActasCon_view(request):
    contenido = GestorPublicaciones.objects.all()
    subtitulo = ""
    dic = {'list_Publicaciones': contenido, 'subtitulo': subtitulo}
    return render(request, "observatorio/Publicaciones/ActasCongresos.html", dic)


def EncuestaFromsG(request):
    subtitulo = ""
    dic = { 'subtitulo': subtitulo}
    return render(request, "observatorio/Encuesta/NuevaEncuesta.html", dic)


def EncuestasCreate(request):
    subtitulo = ""
    dic = {'subtitulo': subtitulo}
    return render(request, "observatorio/Encuesta/EncuestasCreate.html", dic)


def EncuestasCreatePreguntas(request):
    subtitulo = ""
    dic = {'subtitulo': subtitulo}
    return render(request, "observatorio/Encuesta/EncuestaPreguntas.html", dic)
