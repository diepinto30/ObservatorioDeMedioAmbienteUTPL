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
    ('Bloque_1', 'Bloque 1'),
    ('Bloque_2', 'Bloque 2'),
    ('Bloque_3', 'Bloque 3'),
    ('Bloque_4', 'Bloque 4'),
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


TypeParticipante_CHOICES = (
    ('DocenteInvestigador', 'Docente Investigador'),
    ('Estudiantes', 'Estudiantes'),

)

TypeCargo_CHOICES = (
    ('Coordinacion', 'Coordinación'),
    ('DocenteInvestigador', 'Docente Investigador Participante'),
    ('Estudiantes', 'Estudiantes'),

)


Typereque_CHOICES = (
    ('True', 'Verdadero'),
    ('False', 'Falso'),

)

TypePregunta_CHOICES = (
    ('texto', 'Texto'),
    ('TrueOrFalse', 'Verdadero o Falso'),
    ('CheckBox', 'Selección Multiple'),
    ('Check', 'Selección Única'),


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
    img = models.ImageField(upload_to='portal/imgs/', blank=True)
    #img = models.FileField(blank=True)
    Posiciones = models.DecimalField(max_digits=3000, blank=True, decimal_places=1)

    def __str__(self):
        return self.TituloContenido


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

    def __str__(self):
        return self.TituloPublicaciones

    class Meta:
        db_table = 'GestorPublicaciones'


class GestorParticipantes(models.Model):
    idGestorParticipantes = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=4000, blank=False)
    Apellidos = models.CharField(max_length=4000, blank=False)
    TipoParticipante = models.CharField(max_length=4000, blank=False, choices=TypeParticipante_CHOICES)
    TipoCargo = models.CharField(max_length=4000, blank=False, choices=TypeCargo_CHOICES)
    TipoSeccion = models.CharField(max_length=4000, blank=False, choices=TypeSeccion_CHOICES)
    textoAmbitosAccion = RichTextField(blank=True)
    img = models.ImageField(upload_to='portal/Participantes/', blank=True)
    Posiciones = models.DecimalField(max_digits=3000, blank=True, decimal_places=1)

    def __str__(self):
        template = '{0.Nombres} {0.Apellidos} - {0.TipoParticipante} - {0.TipoCargo} - {0.TipoSeccion} - {0.img} - {0.Posiciones}'
        return template.format(self)
    class Meta:
        db_table = 'GestorParticipantes'



class Encuestas(models.Model):
    idEncuestas = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=3000, blank=True)
    seccion = models.CharField(max_length=3000, blank=True)
    descripcion = models.CharField(max_length=5000, blank=True)


    def __str__(self):
        return self.nombre, self.descripcion


    class Meta:
        db_table = 'Encuestas'



class Pregunta(models.Model):
    idPregunta = models.AutoField(primary_key=True)
    nombrePregunta = models.CharField(max_length=4000, blank=True)
    requerida = models.CharField(max_length=11, blank=True, choices=Typereque_CHOICES)
    tipoOpcion = models.CharField(max_length=4000, blank=True, choices=TypePregunta_CHOICES)
    idEncuesta = models.ForeignKey(Encuestas, on_delete=None)

    def __str__(self):
        return self.nombrePregunta, self.tipoOpcion


    class Meta:
        db_table = 'Pregunta'


class Respuestas(models.Model):
    idRespuestas = models.AutoField(primary_key=True)
    idEncuesta = models.ForeignKey(Pregunta, on_delete=None)
    idPreguntas = models.ForeignKey(Encuestas, on_delete=None)
    RespuestaNombres = models.CharField(max_length=4000, blank=False)

    def __str__(self):
        return self.idEncuesta, self.idPreguntas, self.RespuestaNombres


    class Meta:
        db_table = 'Respuestas'


class DataGrupo(models.Model):
    idDataGrupo = models.AutoField(primary_key=True)
    CodigoEncuentas = models.CharField(max_length=10, blank=True)
    Anio = models.CharField(max_length=4)
    Mes = models.CharField(max_length=90)
    Encuestador = models.CharField(max_length=8, blank=True)
    CodigoEncuesta = models.CharField(max_length=8000, blank=True)
    FechaAplicacion = models.CharField(max_length=1000, blank=True)
    Genero = models.CharField(max_length=1000, blank=True)
    edad = models.CharField(max_length=1000, blank=True)
    edad2 = models.CharField(max_length=1000, blank=True)
    NivelEducacion = models.IntegerField(default=0, null=True)
    ClasificacionOcupacionCIUO08 = models.CharField(max_length=1000, blank=True)
    LocalidadVive = models.CharField(max_length=1000, blank=True)
    CantonDondeVive = models.CharField(max_length=1000, blank=True)
    Provincia = models.CharField(max_length=1000, blank=True)
    Sector = models.IntegerField(default=0, null=True)
    SuCasaes = models.CharField(max_length=1000, blank=True)
    Pregunta1 = models.TextField(blank=True)
    r1p1 = models.TextField(blank=True)
    Pregunta2 = models.TextField(blank=True)
    r1p2 = models.TextField(blank=True)
    Pregunta3 = models.TextField(blank=True)
    r1p3 = models.TextField(blank=True)
    Pregunta4 = models.TextField(blank=True)
    r1p4 = models.TextField(blank=True)
    Pregunta5 = models.TextField(blank=True)
    r1p5 = models.TextField(blank=True)
    Pregunta6 = models.TextField(blank=True)
    r1p6 = models.TextField(blank=True)
    Pregunta7 = models.TextField(blank=True)
    r1p7 = models.TextField(blank=True)
    Pregunta8 = models.URLField(blank=True)
    r1p8 = models.TextField(blank=True)
    Pregunta9 = models.URLField(blank=True)
    r1p9 = models.TextField(blank=True)
    Pregunta10 = models.TextField(blank=True)
    r1p10 = models.TextField(blank=True)

    class Meta:
        db_table = 'DataGrupo'
