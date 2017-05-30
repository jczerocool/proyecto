# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here. model to store user data
class Asistencia(models.Model):
	nombres = models.CharField(max_length=120)
	apellidos = models.CharField(max_length=120)
	clase = models.CharField(max_length=120, null=True)
	hora = models.CharField(max_length=8, null=True)
	presente = models.BooleanField(default=True)


	def __unicode__(self):
		return self.nombres
