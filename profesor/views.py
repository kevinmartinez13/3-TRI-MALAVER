# profesor/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Profesor
from .forms import ProfesorForm  # crea forms.py si aún no existe

class ProfesorListView(ListView):
    model = Profesor
    template_name = 'profesor/profesor_list.html'
    context_object_name = 'profesores'

class ProfesorCreateView(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor/profesor_form.html'
    success_url = reverse_lazy('profesor:listar')

class ProfesorDeleteView(DeleteView):
    model = Profesor
    template_name = 'profesor/profesor_confirm_delete.html'
    success_url = reverse_lazy('profesor:listar')

