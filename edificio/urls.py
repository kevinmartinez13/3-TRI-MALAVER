from django.urls import path
from .views import EdificioListView, EdificioCreateView, EdificioDeleteView

app_name = 'edificio'

urlpatterns = [
    path('', EdificioListView.as_view(), name='listar'),
    path('nuevo/', EdificioCreateView.as_view(), name='nuevo'),
    path('borrar/<int:pk>/', EdificioDeleteView.as_view(), name='borrar'),
]