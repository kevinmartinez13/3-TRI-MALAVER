from django.urls import path
from .views import EstudianteListView, EstudianteCreateView, EstudianteDeleteView

app_name = 'estudiante'

urlpatterns = [
    path('', EstudianteListView.as_view(), name='listar'),
    path('nuevo/', EstudianteCreateView.as_view(), name='nuevo'),
    path('borrar/<int:pk>/', EstudianteDeleteView.as_view(), name='borrar'),
]
