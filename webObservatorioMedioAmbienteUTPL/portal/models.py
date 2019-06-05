from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

Type_CHOICES = (
    ('home', 'Home'),
    ('conocenos', 'Conocenos'),
    ('site1', 'site1'),
    ('site2', 'site2'),
    ('site3', 'site3'),
)

TypeSeccion_CHOICES = (
    ('Seccion_1', 'Seccion 1'),
    ('Seccion_2', 'Seccion 2'),
    ('Seccion_3', 'Seccion 3'),
    ('Seccion_4', 'Seccion 4'),
)


class GestorContenidos(models.Model):
    idGestorContenidos = models.AutoField(primary_key=True)
    TituloContenido = models.CharField(max_length=4000, blank=True)
    SubiTituloContenido = models.CharField(max_length=4000, blank=True)
    TipoContenido = models.CharField(max_length=4000, blank=True, choices=Type_CHOICES)
    TipoSeccion = models.CharField(max_length=4000, blank=True, choices=TypeSeccion_CHOICES)
    urlHTML = models.TextField(blank=False)
    # texto = models.TextField(blank=True)
    texto = RichTextField(blank=True)
    img = models.ImageField(upload_to='portal/imgs')
    Posiciones = models.DecimalField(max_digits=3000, blank=False, decimal_places=1)
    class Meta:
        db_table = 'GestorContenidos'
