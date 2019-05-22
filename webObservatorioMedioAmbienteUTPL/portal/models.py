from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class AuthUser(models.Model):
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField('solved time', default=timezone.now)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField('solved time', default=timezone.now)

    def __unicode__(self):
        return "%s - %s - %s - %s - %s" % (self.username, self.first_name, self.last_name, self.email, self.password)


class User(models.Model):
    iduser = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField('solved time', default=timezone.now)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField('solved time', default=timezone.now)

    def __unicode__(self):
        return "%s -%s - %s - %s - %s - %s" % (self.iduser, self.username, self.first_name, self.last_name, self.email, self.password)
