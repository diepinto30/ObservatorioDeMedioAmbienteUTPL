from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^login/$', views.login_user, name="login"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout_view/$', views.logout_view, name="logout_view"),
    url(r'^conocenos/$', views.conocenos, name="conocenos"),
    url(r'^GestorContenido/$', views.GestorContenido, name="GestorContenido"),
]
