from itertools import starmap
from logging import disable
from django import forms
from django.contrib.auth.management import get_default_username
from django.contrib.auth.models import User
from .models import GestorContenidos, GestorPublicaciones
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class SignUp(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'usermane'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'nombres'}), max_length=30, required=True,
                                 help_text='Optional.')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'apellidos'}), max_length=30,
                                required=True, help_text='Optional.')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'ejemplo@gmail.com'}), max_length=254,
                             help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class LoginFrom(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')




class ContenidoFrom(forms.ModelForm):
    Type_CHOICES = (
        ('Seleccione ...', 'Seleccione ...'),
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
        ('Seleccione ...', 'Seleccione ...'),
        ('Seccion_1', 'Seccion 1'),
        ('Seccion_2', 'Seccion 2'),
        ('Seccion_3', 'Seccion 3'),
        ('Seccion_4', 'Seccion 4'),
    )

    TituloContenido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    SubiTituloContenido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    TipoContenido = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), required=True, choices=Type_CHOICES)
    TipoSeccion = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), required=True, choices=TypeSeccion_CHOICES)
    urlHTML = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    # texto = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)
    # texto = forms.CharField(widget= RichTextField(blank=True))
    texto = forms.CharField(widget=CKEditorWidget(attrs={'id': 'editor'}), required=True)
    # img = forms.ImageField(widget=forms.ImageField(attrs={'name': 'document'}))
    #img = forms.FileField()
    class Meta:
        model = GestorContenidos
        fields = ('TituloContenido', 'SubiTituloContenido', 'TipoContenido', 'TipoSeccion', 'urlHTML', 'texto', 'img')


class PublicacionesFrom(forms.ModelForm):
    Type2_CHOICES = (
        ('Seleccione ...', 'Seleccione ...'),
        ('home', 'Home'),
        ('conocenos', 'Conocenos'),
        ('site_Revistas_indexadas', 'Página - Revistas indexadas'),
        ('site_Articulos_Divulgacion', 'Página - Artículos de Divulgación'),
        ('site_CalidadDeVida', 'Página - Calidad de Vida'),
        ('site_Ponencias', 'Página - Ponencias'),
        ('site_Tesis', 'Página - Tesis'),
    )


    TypeSeccion_CHOICES = (
        ('Seleccione ...', 'Seleccione ...'),
        ('Seccion_1', 'Seccion 1'),
        ('Seccion_2', 'Seccion 2'),
        ('Seccion_3', 'Seccion 3'),
        ('Seccion_4', 'Seccion 4'),
    )

    TituloPublicaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    SubiTituloPublicaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    TipoContenido = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), required=True, choices=Type2_CHOICES)
    TipoSeccion = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), required=True, choices=TypeSeccion_CHOICES)
    texto = forms.CharField(widget=CKEditorWidget(attrs={'id': 'editor'}), required=True)

    class Meta:
        model = GestorPublicaciones
        fields = ('TituloPublicaciones', 'SubiTituloPublicaciones', 'TipoContenido', 'TipoSeccion', 'texto')
