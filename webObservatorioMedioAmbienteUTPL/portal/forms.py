from itertools import starmap
from logging import disable
from django import forms
from django.contrib.auth.management import get_default_username
from django.contrib.auth.models import User
from .models import GestorContenidos
from django.contrib.auth.forms import UserCreationForm


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
        ('site1', 'site1'),
        ('site2', 'site2'),
        ('site3', 'site3'),
    )
    TituloContenido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    SubiTituloContenido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    TipoContenido = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), required=True, choices=Type_CHOICES)
    texto = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)
    img = forms.ImageField(required=False)

    class Meta:
        model = GestorContenidos
        fields = ('TituloContenido', 'SubiTituloContenido', 'TipoContenido', 'texto', 'img')
        labels = {'TituloContenido': 'Titulo del Contenido', }
