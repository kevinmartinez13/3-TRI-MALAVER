from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from .models import Aula
from .forms import AulaForm

def aula_list(request):
    aulas = Aula.objects.select_related('edificio').all().order_by('numero')
    return render(request, 'aula/aula_list.html', {'aulas': aulas})

def aula_create(request):
    if request.method == 'POST':
        form = AulaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aula creada correctamente.')
            return redirect('aula:listar')
    else:
        form = AulaForm()
    return render(request, 'aula/aula_form.html', {'form': form})

def aula_confirm_delete(request, pk):
    aula = get_object_or_404(Aula, pk=pk)
    if request.method == 'POST':
        # Eliminar permanentemente de la DB
        aula.delete()
        messages.success(request, 'Aula borrada permanentemente.')
        return redirect('aula:listar')
    return render(request, 'aula/aula_confirm_delete.html', {'aula': aula})
