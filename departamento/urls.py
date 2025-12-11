from django.urls import path
from .views import DepartamentoListView, DepartamentoCreateView, DepartamentoDeleteView

app_name = 'departamento'

urlpatterns = [
    path('', DepartamentoListView.as_view(), name='listar'),
    path('nuevo/', DepartamentoCreateView.as_view(), name='nuevo'),
    path('borrar/<int:pk>/', DepartamentoDeleteView.as_view(), name='borrar'),
]
