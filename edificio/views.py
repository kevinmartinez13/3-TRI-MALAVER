from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Edificio
from .forms import EdificioForm

class EdificioListView(ListView):
    model = Edificio
    template_name = 'edificio/edificio_list.html'
    context_object_name = 'edificios'

class EdificioCreateView(CreateView):
    model = Edificio
    form_class = EdificioForm
    template_name = 'edificio/edificio_form.html'
    success_url = reverse_lazy('edificio:listar')

class EdificioDeleteView(DeleteView):
    model = Edificio
    template_name = 'edificio/edificio_confirm_delete.html'
    success_url = reverse_lazy('edificio:listar')