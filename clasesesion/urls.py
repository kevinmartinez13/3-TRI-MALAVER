from django.urls import path
from .views import ClaseSesionListView, ClaseSesionCreateView, ClaseSesionDeleteView

app_name = 'clasesesion'

urlpatterns = [
    path('', ClaseSesionListView.as_view(), name='sesion_list'),
    path('nuevo/', ClaseSesionCreateView.as_view(), name='sesion_nuevo'),
    path('borrar/<int:pk>/', ClaseSesionDeleteView.as_view(), name='sesion_borrar'),
]
