# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Asistencia

class ListaAdmin(admin.ModelAdmin):
    class Meta:
        model = Asistencia

admin.site.register(Asistencia, ListaAdmin)
