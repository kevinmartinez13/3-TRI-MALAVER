from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Estudiante
from .forms import EstudianteForm

class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiante/estudiante_list.html'
    context_object_name = 'estudiantes'

class EstudianteCreateView(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'estudiante/estudiante_form.html'
    success_url = reverse_lazy('estudiante:listar')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'estudiante/estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiante:listar')
