from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Matricula
from .forms import MatriculaForm

class MatriculaListView(ListView):
    model = Matricula
    template_name = 'matricula/matricula_list.html'
    context_object_name = 'matriculas'

class MatriculaCreateView(CreateView):
    model = Matricula
    form_class = MatriculaForm
    template_name = 'matricula/matricula_form.html'
    success_url = reverse_lazy('matricula:listar')

class MatriculaDeleteView(DeleteView):
    model = Matricula
    template_name = 'matricula/matricula_confirm_delete.html'
    success_url = reverse_lazy('matricula:listar')
