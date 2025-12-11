from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from .models import Calificacion
from .forms import CalificacionForm

class CalificacionListView(ListView):
    model = Calificacion
    template_name = 'calificacion/calificacion_list.html'
    context_object_name = 'calificaciones'

class CalificacionCreateView(CreateView):
    model = Calificacion
    form_class = CalificacionForm
    template_name = 'calificacion/calificacion_form.html'
    success_url = reverse_lazy('calificacion:list')

class CalificacionDetailView(DetailView):
    model = Calificacion
    template_name = 'calificacion/calificacion_detail.html'
    context_object_name = 'calificacion'

class CalificacionDeleteView(DeleteView):
    model = Calificacion
    template_name = 'calificacion/calificacion_confirm_delete.html'
    success_url = reverse_lazy('calificacion:list')
