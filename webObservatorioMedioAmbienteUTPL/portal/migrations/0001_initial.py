# Generated by Django 2.1 on 2019-05-28 01:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='solved time')),
                ('is_superuser', models.BooleanField()),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='solved time')),
            ],
        ),
        migrations.CreateModel(
            name='GestorContenidos',
            fields=[
                ('idGestorContenidos', models.AutoField(primary_key=True, serialize=False)),
                ('TituloContenido', models.CharField(blank=True, max_length=8)),
                ('SubiTituloContenido', models.CharField(blank=True, max_length=8000)),
                ('TipoContenido', models.CharField(blank=True, max_length=1000)),
                ('texto', models.TextField(blank=True)),
                ('img', models.ImageField(blank=True, upload_to='portal/imgs')),
            ],
            options={
                'db_table': 'GestorContenidos',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('iduser', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='solved time')),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='solved time')),
            ],
        ),
    ]