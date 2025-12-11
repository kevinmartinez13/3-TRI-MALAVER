from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from .models import ClaseSesion
from .forms import ClaseSesionForm

class ClaseSesionListView(ListView):
    model = ClaseSesion
    template_name = 'clasesesion/clasesesion_list.html'
    context_object_name = 'sesiones'

class ClaseSesionCreateView(CreateView):
    model = ClaseSesion
    form_class = ClaseSesionForm
    template_name = 'clasesesion/clasesesion_form.html'
    success_url = reverse_lazy('clasesesion:sesion_list')

class ClaseSesionDeleteView(DeleteView):
    model = ClaseSesion
    template_name = 'clasesesion/clasesesion_confirm_delete.html'
    success_url = reverse_lazy('clasesesion:sesion_list')
