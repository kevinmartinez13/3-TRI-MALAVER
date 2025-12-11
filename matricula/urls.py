from django.urls import path
from .views import MatriculaListView, MatriculaCreateView, MatriculaDeleteView

app_name = 'matricula'

urlpatterns = [
    path('', MatriculaListView.as_view(), name='listar'),
    path('nuevo/', MatriculaCreateView.as_view(), name='nuevo'),
    path('borrar/<int:pk>/', MatriculaDeleteView.as_view(), name='borrar'),
]