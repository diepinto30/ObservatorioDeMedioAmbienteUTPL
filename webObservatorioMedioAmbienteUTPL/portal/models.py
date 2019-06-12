from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

Type_CHOICES = (
    ('home', 'Home'),
    ('conocenos', 'Conocenos'),
    ('site_Agua', 'Página - Agua'),
    ('site_MedioAmbiente', 'Página - Medio Ambiente'),
    ('site_CalidadDeVida', 'Página - Calidad de Vida'),
    ('site_Equidad', 'Página - Equidad'),
    ('site_Mercados', 'Página - Mercados'),
    ('site_ParticipacionDemocracia', 'Página - Participación y democracia'),
    ('site_Etnozoologia', 'Página - Etnozoología'),
    ('site_12', 'Página -'),
    ('site_', 'Página -'),
    ('site_', 'Página -'),
)

TypeSeccion_CHOICES = (
    ('Seccion_1', 'Seccion 1'),
    ('Seccion_2', 'Seccion 2'),
    ('Seccion_3', 'Seccion 3'),
    ('Seccion_4', 'Seccion 4'),
)


Type2_CHOICES = (
    ('home', 'Home'),
    ('conocenos', 'Conocenos'),
    ('site_Revistas_indexadas', 'Página - Revistas indexadas'),
    ('site_Articulos_Divulgacion', 'Página - Artículos de Divulgación'),
    ('site_CalidadDeVida', 'Página - Calidad de Vida'),
    ('site_Ponencias', 'Página - Ponencias'),
    ('site_Tesis', 'Página - Tesis'),
)



class GestorContenidos(models.Model):
    idGestorContenidos = models.AutoField(primary_key=True)
    TituloContenido = models.CharField(max_length=4000, blank=True)
    SubiTituloContenido = models.CharField(max_length=4000, blank=True)
    TipoContenido = models.CharField(max_length=4000, blank=True, choices=Type_CHOICES)
    TipoSeccion = models.CharField(max_length=4000, blank=True, choices=TypeSeccion_CHOICES)
    urlHTML = models.TextField(blank=True)
    # texto = models.TextField(blank=True)
    texto = RichTextField(blank=True)
    # img = models.ImageField(upload_to='portal/imgs', blank=True)
    img = models.FileField(blank=True)
    Posiciones = models.DecimalField(max_digits=3000, blank=True, decimal_places=1)

    def __unicode__(self):
        return "%s - %s" % (self.idGestorContenidos, self.TituloContenido)


    class Meta:
        db_table = 'GestorContenidos'


class GestorPublicaciones(models.Model):
    idGestorPublicaciones = models.AutoField(primary_key=True)
    TituloPublicaciones = models.CharField(max_length=4000, blank=True)
    SubiTituloPublicaciones = models.CharField(max_length=4000, blank=True)
    TipoContenido = models.CharField(max_length=4000, blank=True, choices=Type2_CHOICES)
    TipoSeccion = models.CharField(max_length=4000, blank=True, choices=TypeSeccion_CHOICES)
    texto = RichTextField(blank=True)
    Posiciones = models.DecimalField(max_digits=3000, blank=True, decimal_places=1)

    class Meta:
        db_table = 'GestorPublicaciones'


