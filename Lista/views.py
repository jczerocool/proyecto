# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.http import Http404
from django.shortcuts import get_object_or_404

from .forms import AsistenciaForm
from .models import Asistencia
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.db.models import Q


# Create your views here.
def agregar_alumno(request):
    #FORM
    form = AsistenciaForm(request.POST or None)
    if request.method == "POST":
        print request.POST
    if form.is_valid():
        # print request.POST
        data = form.cleaned_data
        nombres = data.get("nombres")
        apellidos = data.get("apellidos")
        clase = data.get("clase")
        hora = data.get("hora")
        # presente = data.get()


        nuevo_alumno = Asistencia()
        nuevo_alumno.nombres = nombres
        nuevo_alumno.apellidos = apellidos
        nuevo_alumno.clase = clase
        nuevo_alumno.hora = hora
        # nuevo_alumno.presente = presente

        nuevo_alumno.save()
        return redirect("/asistenciaview/")
    template = "agregar_alumno.html"
    context = {"form": AsistenciaForm}




    return render(request, template, context)



class asistenciaview(ListView):
    model = Asistencia
    def get_queryset(self, *args, **kwargs):
        qs=super(asistenciaview, self).get_queryset(**kwargs)
        query = self.request.GET.get('q')
        if query:
            qset = (
                Q(nombres__icontains=query) |
                Q(apellidos__icontains=query) |
                Q(clase__icontains=query) |
                Q(hora__icontains=query) |
                Q(presente__icontains=query)

            )
            qs = Asistencia.objects.filter(qset).distinct()

        return qs


class AsistenciaUpdate(UpdateView):
    # print "UPDATE"
    model = Asistencia
    # form_class = AsistenciaForm
    fields = ["nombres", "apellidos", "clase", "hora", "presente"]
    template = "agregar_alumno.html"
    success_url = "/asistenciaview/"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(AsistenciaUpdate, self).get_context_data(*args, **kwargs)
    #     context["submit_btn"]="Editar"
    #     return context

# def modificar_alumno(request, object_id=None):
#     #Logico de negocio alias hechizo
#     lista = get_object_or_404 (Asistencia, id = object_id)
#     form = AsistenciaForm(request.POST or None, instance=lista)
#     if form.is_valid():
#         form.save()
#         print "Actualizacion exitosa!"
#     template = "update.html"
#     contexto= {
#            "Lista": Asistencia,
#            "form": form,
#            "titulo":" Actualizar alumno"
#            }
#     return render(request, template, contexto)



def home(request):
    context = {}
    template = 'home.html'
    return render(request,template,context)

def about(request):
    context = {}
    template = 'about.html'
    return render(request,template,context)

@login_required
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request,template,context)
