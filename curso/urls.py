from django.urls import path
from .views import CursoListView, CursoCreateView, CursoDeleteView

app_name = 'curso'

urlpatterns = [
    path('', CursoListView.as_view(), name='curso_list'),
    path('nuevo/', CursoCreateView.as_view(), name='curso_nuevo'),
    path('borrar/<int:pk>/', CursoDeleteView.as_view(), name='curso_borrar'),
]
