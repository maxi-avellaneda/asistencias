from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import PersonaForm
from .models import Persona

# Create your views here.

def crear_persona(request):
    if request.method == 'POST':
        programa_form = PersonaForm(request.POST, request.FILES)
        if programa_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            programa_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente la persona')
            return redirect(reverse('persona:listar_personas'))
    else:
        programa_form = PersonaForm()

    return render(request, 'persona/crear_persona.html',
                  {'form': programa_form})

def lista_personas(request):
    programas = Persona.objects.all()
    return render(request, 'persona/listar_personas.html',
                  {'programas': programas})