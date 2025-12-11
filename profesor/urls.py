# profesor/urls.py
from django.urls import path
from .views import ProfesorListView, ProfesorCreateView, ProfesorDeleteView

app_name = 'profesor'

urlpatterns = [
    path('', ProfesorListView.as_view(), name='listar'),
    path('nuevo/', ProfesorCreateView.as_view(), name='nuevo'),
    path('borrar/<int:pk>/', ProfesorDeleteView.as_view(), name='borrar'),
]
