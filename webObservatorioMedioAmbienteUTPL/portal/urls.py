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
]
