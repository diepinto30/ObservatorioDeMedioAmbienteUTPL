from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^login/$', views.login_user, name="login"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout_view/$', views.logout_view, name="logout_view"),
    url(r'^conocenos/$', views.conocenos, name="conocenos"),
    url(r'^GestorContenido/$', views.GestorContenido, name="GestorContenido"),
    url(r'^Contenido_edit/(?P<id>\d+)/$', views.Contenido_edit, name='Contenido_edit'),
    url(r'^EliminarContenido/(?P<id>\d+)/$', views.EliminarContenido, name='EliminarContenido'),
    url(r'^Componentes/Agua/$', views.Agua_view, name='Agua_view'),
    url(r'^Componentes/MedioAmbiente/$', views.MedioAmbiente_view, name='MedioAmbiente_view'),
    url(r'^Componentes/CalidadDeVida/$', views.CalidadDeVida_view, name='CalidadDeVida_view'),
    url(r'^Componentes/Equidad/$', views.Equidad_view, name='Equidad_view'),
    url(r'^Componentes/Mercados/$', views.Mercados_view, name='Mercados_view'),
    url(r'^Componentes/Participacion_Y_Democracia/$', views.ParticipacionDemocracia_view, name='ParticipacionDemocracia_view'),
    url(r'^Componentes/Etnozoologia/$', views.Etnozoologia_view, name='Etnozoologia_view'),

]
