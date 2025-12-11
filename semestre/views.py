from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import Semestre
from .forms import SemestreForm

class SemestreListView(ListView):
    model = Semestre
    template_name = 'semestre/semestre_list.html'
    context_object_name = 'semestres'

class SemestreCreateView(CreateView):
    model = Semestre
    form_class = SemestreForm
    template_name = 'semestre/semestre_form.html'
    success_url = reverse_lazy('semestre:listar')

class SemestreDeleteView(DeleteView):
    model = Semestre
    template_name = 'semestre/semestre_confirm_delete.html'
    success_url = reverse_lazy('semestre:listar')

