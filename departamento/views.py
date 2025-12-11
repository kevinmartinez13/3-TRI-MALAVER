from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Departamento
from .forms import DepartamentoForm

class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamento/departamento_list.html'
    context_object_name = 'departamentos'

class DepartamentoCreateView(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/departamento_form.html'
    success_url = reverse_lazy('departamento:listar')

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = 'departamento/departamento_confirm_delete.html'
    success_url = reverse_lazy('departamento:listar')
