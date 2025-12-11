"""
URL configuration for servidorcolegio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
     path('aulas/', include('aula.urls', namespace='aula')),
     path('calificacion/', include('calificacion.urls')),
     path('clasesesion/', include('clasesesion.urls', namespace='clasesesion')),
     path('curso/', include('curso.urls', namespace='curso')),
     path('departamento/', include('departamento.urls', namespace='departamento')),
     path('edificio/', include('edificio.urls', namespace='edificio')),
     path('estudiante/', include('estudiante.urls', namespace='estudiante')),
     path('matricula/', include('matricula.urls', namespace='matricula')),
     path('profesor/', include('profesor.urls', namespace='profesor')),
     path('semestre/', include('semestre.urls', namespace='semestre')),


     


]
