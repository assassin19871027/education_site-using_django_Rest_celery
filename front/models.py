# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_comments_xtd.models import XtdComment

# Create your models here.



class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, help_text=u'Sube una foto de no mas de 2mb y de una resolución maxima 1280x1280.')
    headline = models.CharField(max_length=200, help_text=u'Breve description de hasta 200 caracteres.')
    about = models.TextField(help_text=u'Cuentales a tus alumnos por que deberian tomar la clase contigo')
#    position = GeopositionField()
    fee = models.FloatField(help_text=u'El monto minimo es $CL2.000 y maximo es $CL50.000 por hora')
    stars = models.IntegerField(blank=True, null=True)
    skills = models.ManyToManyField("Skill", help_text=u'Cuentanos en que asignaturas quieres ser profesor')

#    ping = models.DateTimeField(default=timezone.now)
#    lastseen = models.DateTimeField(default=timezone.now)

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s" % self.name


class SlimComment(XtdComment):
    title = models.CharField(max_length=256)