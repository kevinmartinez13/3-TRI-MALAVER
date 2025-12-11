from django.urls import path
from .views import (
    CalificacionListView, CalificacionCreateView,
    CalificacionDetailView, CalificacionDeleteView
)

app_name = 'calificacion'

urlpatterns = [
    path('', CalificacionListView.as_view(), name='list'),
    path('nuevo/', CalificacionCreateView.as_view(), name='create'),
    path('<int:pk>/', CalificacionDetailView.as_view(), name='detail'),
    path('<int:pk>/borrar/', CalificacionDeleteView.as_view(), name='delete'),
]