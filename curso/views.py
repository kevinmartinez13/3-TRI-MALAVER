from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Curso
from .forms import CursoForm

class CursoListView(ListView):
    model = Curso
    template_name = 'curso/curso_list.html'
    context_object_name = 'cursos'

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso/curso_form.html'
    success_url = reverse_lazy('curso:curso_list')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'curso/curso_confirm_delete.html'
    success_url = reverse_lazy('curso:curso_list')
