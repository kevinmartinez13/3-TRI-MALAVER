from django.urls import path
from .views import SemestreListView, SemestreCreateView, SemestreDeleteView

app_name = 'semestre'

urlpatterns = [
    path('', SemestreListView.as_view(), name='listar'),
    path('nuevo/', SemestreCreateView.as_view(), name='nuevo'),
    path('borrar/<int:pk>/', SemestreDeleteView.as_view(), name='borrar'),
]

