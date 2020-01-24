from django.db.models import Count
from django.shortcuts import render, redirect, render_to_response
from .forms import LoginFrom, SignUp, ContenidoFrom, PublicacionesFrom, ParticipantesFrom, NameEncuestaFrom, NamePreguntaFrom, RealizarEncuestaFrom
from django.contrib.auth import login, authenticate, logout
from .models import GestorContenidos, Pregunta
from .models import Encuestas, DataGrupo
from .models import GestorPublicaciones, GestorParticipantes
from django.urls import reverse
from django.http import HttpResponseRedirect


def home(request):
    contenido = GestorContenidos.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo}
    return render(request, "home.html", dic)


def conocenos(request):
    contenido = GestorContenidos.objects.all()
    participantes = GestorParticipantes.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo, 'list_participantes': participantes}
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
        form = ContenidoFrom(request.POST, request.FILES)
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
        form = ContenidoFrom(request.POST, request.FILES, instance=Contenido)
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
        form = ParticipantesFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"
        return redirect("/")
    else:
        form = ParticipantesFrom()
    return render(request, 'observatorio/GestorContenido/GestorParticipantes.html', {'form': form})


def Participantes_edit(request, id):
    Contenido = GestorParticipantes.objects.get(idGestorParticipantes=id)
    if request.method == 'GET':
        form = ParticipantesFrom(instance=Contenido)
    else:
        form = ParticipantesFrom(request.POST, request.FILES, instance=Contenido)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request, 'observatorio/GestorContenido/EditorDeParticipantes.html', {'form': form})


def EliminarParticipantes(request, id):
    Contenido = GestorParticipantes.objects.get(idGestorParticipantes=id)
    if request.method == 'POST':
        Contenido.delete()
        return redirect("/")
    return render(request, 'observatorio/GestorContenido/EliminarDeParticipantes.html', {'Contenido': Contenido})


# sitios de los contenido
def Agua_view(request):
    contenido = GestorContenidos.objects.all()
    subtitulo = ""
    # estadista agua
    #total = DataGrupo.objects.annotate(Count('r1p1', Avg('r1p1')))

    # pregunta 1
    viven14 = DataGrupo.objects.filter(r1p1='1-4').annotate(Count('r1p1'))
    viven58 = DataGrupo.objects.filter(r1p1='5-8').annotate(Count('r1p1'))
    viven910 = DataGrupo.objects.filter(r1p1='9-10').annotate(Count('r1p1'))
    vivenDes = DataGrupo.objects.filter(r1p1='').annotate(Count('r1p1'))

    # pregunta 2
    ## año 2016
    ingre366_16 = DataGrupo.objects.filter(r1p2='<366', Anio='2016').annotate(Count('Anio'))
    ingre366500_16 = DataGrupo.objects.filter(r1p2='366 - <500', Anio='2016').annotate(Count('Anio'))
    ingre5001000_16 = DataGrupo.objects.filter(r1p2='500 - <1000', Anio='2016').annotate(Count('Anio'))
    ingre10002000_16 = DataGrupo.objects.filter(r1p2='1000 - <2000', Anio='2016').annotate(Count('Anio'))
    ingre200_16 = DataGrupo.objects.filter(r1p2='>2000', Anio='2016').annotate(Count('Anio'))
     ## año 2017
    ingre366_17 = DataGrupo.objects.filter(r1p2='<366', Anio='2017').annotate(Count('Anio'))
    ingre366500_17 = DataGrupo.objects.filter(r1p2='366 - <500', Anio='2017').annotate(Count('Anio'))
    ingre5001000_17 = DataGrupo.objects.filter(r1p2='500 - <1000', Anio='2017').annotate(Count('Anio'))
    ingre10002000_17 = DataGrupo.objects.filter(r1p2='1000 - <2000', Anio='2017').annotate(Count('Anio'))
    ingre200_17 = DataGrupo.objects.filter(r1p2='>2000', Anio='2017').annotate(Count('Anio'))
     ## año 2018
    ingre366_18 = DataGrupo.objects.filter(r1p2='<366', Anio='2018').annotate(Count('Anio'))
    ingre366500_18 = DataGrupo.objects.filter(r1p2='366 - <500', Anio='2018').annotate(Count('Anio'))
    ingre5001000_18 = DataGrupo.objects.filter(r1p2='500 - <1000', Anio='2018').annotate(Count('Anio'))
    ingre10002000_18 = DataGrupo.objects.filter(r1p2='1000 - <2000', Anio='2018').annotate(Count('Anio'))
    ingre200_18 = DataGrupo.objects.filter(r1p2='>2000', Anio='2018').annotate(Count('Anio'))

    # pregunta 3
    ## año 2016
    terminoEsNo16 = DataGrupo.objects.filter(r1p4='He escuchado pero no se lo que significa', Anio='2016').annotate(Count('Anio'))
    terminoEsSi16 = DataGrupo.objects.filter(r1p4='He escuchado y se lo que significa', Anio='2016').annotate(Count('Anio'))
    terminoNose16 = DataGrupo.objects.filter(r1p4='No lo sé', Anio='2016').annotate(Count('Anio'))
    ## año 2017
    terminoEsNo17 = DataGrupo.objects.filter(r1p4='He escuchado pero no se lo que significa', Anio='2017').annotate(Count('Anio'))
    terminoEsSi17 = DataGrupo.objects.filter(r1p4='He escuchado y se lo que significa', Anio='2017').annotate(Count('Anio'))
    terminoNose17 = DataGrupo.objects.filter(r1p4='No lo sé', Anio='2017').annotate(Count('Anio'))



    dic = {'list_contenido': contenido, 'subtitulo': subtitulo, 'viven14': viven14, 'viven58': viven58,
           'viven910': viven910, 'vivenDes': vivenDes, 'ingre366_16': ingre366_16, 'ingre366500_16': ingre366500_16,
           'ingre5001000_16': ingre5001000_16, 'ingre10002000_16': ingre10002000_16, 'ingre200_16': ingre200_16,
           'ingre366_17': ingre366_17, 'ingre366500_17': ingre366500_17, 'ingre5001000_17': ingre5001000_17,
           'ingre10002000_17': ingre10002000_17, 'ingre200_17': ingre200_17, 'ingre366_18': ingre366_18,
           'ingre366500_18': ingre366500_18, 'ingre5001000_18': ingre5001000_18, 'ingre10002000_18': ingre10002000_18,
           'ingre200_18': ingre200_18, 'terminoEsNo16': terminoEsNo16, 'terminoEsSi16': terminoEsSi16, 'terminoNose16': terminoNose16,
           'terminoEsNo17': terminoEsNo17, 'terminoEsSi17': terminoEsSi17, 'terminoNose17': terminoNose17 }
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


# gestor de las encuentas
def EncuestaFromsG(request):
    if request.method == 'POST':
        form = NameEncuestaFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('EncuestasCreatePreguntas')
    else:
        form = NameEncuestaFrom()
    return render(request, 'observatorio/Encuesta/NuevaEncuesta.html', {'form': form})


def EncuestasCreatePreguntas(request):
    print("lISDugfb")
    valorUltimo = [Encuestas.objects.latest('idEncuestas')]
    subtitulo = ""
    print("hola: ", valorUltimo)

    if request.method == 'POST':
        form = NamePreguntaFrom(request.POST)
        if form.is_valid():
            form.save()
        return redirect('EncuestasCreatePreguntas')
    else:
        form = NamePreguntaFrom()
    dic = {'subtitulo': subtitulo, 'valorUltimo': valorUltimo, 'form': form}
    return render(request, 'observatorio/Encuesta/EncuestaPreguntas.html', dic)


def EncuestasCreate(request):
    subtitulo = ""
    dic = {'subtitulo': subtitulo}
    return render(request, "observatorio/Encuesta/EncuestasCreate.html", dic)


def Encuestas_list(request):
    encuestas = Encuestas.objects.all()
    subtitulo = ""
    dic = {'subtitulo': subtitulo, 'list_encuestas': encuestas}
    return render(request, "observatorio/Encuesta/ListEncuestas.html", dic)


def Encuestas_edit(request, id):
    Encuesta = Encuestas.objects.get(idEncuestas=id)
    if request.method == 'GET':
        form = ContenidoFrom(instance=Encuesta)
    else:
        form = ContenidoFrom(request.POST, instance=Encuesta)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'observatorio/Encuesta/EditorDeEncuestas.html', {'form': form})


def EliminarEncuesta(request, id):
    Encuesta = Encuestas.objects.get(idEncuestas=id)
    if request.method == 'POST':
        Encuesta.delete()
        return redirect('/')
    return render(request, 'observatorio/Encuesta/EliminarEncuesta.html', {'Encuesta': Encuesta})


def RealizarEncuestas(request, id):
    if request.method == 'POST':
        form = RealizarEncuestaFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"
        return redirect("/")
    else:
        form = RealizarEncuestaFrom()
    return render(request, 'observatorio/Encuesta/RealizarEncuesta.html', {'form': form})


def EncuestaGoogle(request):
    contenido = GestorContenidos.objects.all()
    participantes = GestorParticipantes.objects.all()
    subtitulo = ""
    dic = {'list_contenido': contenido, 'subtitulo': subtitulo, 'list_participantes': participantes}
    return render(request, "observatorio/Encuesta/EncuestaGoogle.html", dic)


