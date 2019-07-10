from django.conf.urls import url
from . import views

urlpatterns = [

    # url del manejo de roles
    url(r'^login/$', views.login_user, name="login"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout_view/$', views.logout_view, name="logout_view"),
    url(r'^conocenos/$', views.conocenos, name="conocenos"),

    # url Gestor Contenido
    url(r'^GestorContenido/$', views.GestorContenido, name="GestorContenido"),
    url(r'^Contenido_edit/(?P<id>\d+)/$', views.Contenido_edit, name='Contenido_edit'),
    url(r'^EliminarContenido/(?P<id>\d+)/$', views.EliminarContenido, name='EliminarContenido'),

    # url Gestor Publicaciones
    url(r'^GestorPublicaciones/$', views.GestorPublicacion, name="GestorPublicacion"),
    url(r'^Publicaciones_edit/(?P<id>\d+)/$', views.Publicaciones_edit, name='Publicaciones_edit'),
    url(r'^EliminarPublicaciones/(?P<id>\d+)/$', views.EliminarPublicaciones, name='EliminarPublicaciones'),

    # url Gestor Participante
    url(r'^GestorParticipantes/$', views.GestorParticipantess, name="GestorParticipantess"),

    # url de las encuesta
    url(r'^EncuestaNuevaGeneral/$', views.EncuestaFromsG, name="EncuestaFromsG"),
    url(r'^EncuestasCreate/$', views.EncuestasCreate, name="EncuestasCreate"),
    url(r'^EncuestasCreatePreguntas/$', views.EncuestasCreatePreguntas, name="EncuestasCreatePreguntas"),
    url(r'^ListarEncuestas/$', views.Encuestas_list, name="Encuestas_list"),


    # url de los sitio principales de la app
    url(r'^Componentes/Agua/$', views.Agua_view, name='Agua_view'),
    url(r'^Componentes/MedioAmbiente/$', views.MedioAmbiente_view, name='MedioAmbiente_view'),
    url(r'^Componentes/CalidadDeVida/$', views.CalidadDeVida_view, name='CalidadDeVida_view'),
    url(r'^Componentes/Equidad/$', views.Equidad_view, name='Equidad_view'),
    url(r'^Componentes/Mercados/$', views.Mercados_view, name='Mercados_view'),
    url(r'^Componentes/Participacion_Y_Democracia/$', views.ParticipacionDemocracia_view, name='ParticipacionDemocracia_view'),
    url(r'^Componentes/Etnozoologia/$', views.Etnozoologia_view, name='Etnozoologia_view'),

    # url de los sitio publicaciones
    url(r'^Publicaciones/RevistasIndexadas/$', views.RevistasIn_view, name='RevistasIn_view'),
    url(r'^Publicaciones/Tesis/$', views.Tesis_view, name='Tesis_view'),
    url(r'^Publicaciones/ArticulosDivulgados/$', views.ArticulosDiv_view, name='ArticulosDiv_view'),
    url(r'^Publicaciones/ActasCongresos/$', views.ActasCon_view, name='ActasCon_view'),

]
