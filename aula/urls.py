from django.urls import path
from . import views

app_name = 'aula'

urlpatterns = [
    path('', views.aula_list, name='listar'),
    path('nuevo/', views.aula_create, name='crear'),
    path('<int:pk>/borrar/', views.aula_confirm_delete, name='borrar'),
]
