"""smartlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from Lista import views as Lista_views
from contact import views as contact_views
from Lista import views
from Lista.views import asistenciaview, AsistenciaUpdate

urlpatterns = [
    url(r'^$', Lista_views.home, name='home'),
    url(r'^about/$', Lista_views.about, name='about'),
    url(r'^profile/$', Lista_views.userProfile, name='profile'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^agregar_alumno/$', views.agregar_alumno, name='agregar_alumno'),
    url(r'^asistenciaview/$', asistenciaview.as_view(), name='asistenciaview'),
    #url(r'^modificar_alumno/$', asistenciaupdate.as_view(), name='asistenciaupdate'),
    url(r'^modificar_alumno/(?P<pk>\d+)/$', AsistenciaUpdate.as_view(), name='modificar_alumno'),

    url(r'^admin/', admin.site.urls),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
