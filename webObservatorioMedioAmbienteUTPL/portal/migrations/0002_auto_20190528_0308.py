# Generated by Django 2.1 on 2019-05-28 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]