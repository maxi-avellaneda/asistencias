from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import ProgramaForm,AsignacionBeneficioForm,tipoAsistenciaForm
from .models import Programa,AsignacionBeneficio,TipoAsistencia


def programa_lista(request):
    programas = Programa.objects.all()
    return render(request, 'programa/lista.html',
                  {'programas': programas})


def programa_detalle(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    return render(request,
                  'programa/detalle.html',
                  {'programa': programa})


def programa_create(request):
    nuevo_programa = None
    if request.method == 'POST':
        programa_form = ProgramaForm(request.POST, request.FILES)
        if programa_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nuevo_programa = programa_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el Programa {}'.format(nuevo_programa))
            return redirect(reverse('programa:programa_detalle', args={nuevo_programa.id}))
    else:
        programa_form = ProgramaForm()

    return render(request, 'programa/programa_form.html',
                  {'form': programa_form})


def programa_delete(request):
    if request.method == 'POST':
        if 'id_programa' in request.POST:
            programa = get_object_or_404(Programa, pk=request.POST['id_programa'])
            nombre_programa = programa.nombre
            programa.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Programa {}'.format(nombre_programa))
        else:
            messages.error(request, 'Debe indicar qué Programa se desea eliminar')
    return redirect(reverse('programa:programa_lista'))


def programa_edit(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    if request.method == 'POST':
        form_programa = ProgramaForm(request.POST, request.FILES, instance=programa)
        if form_programa.is_valid():
            form_programa.save()
            messages.success(request, 'Se ha actualizado correctamente el Programa')
            return redirect(reverse('programa:programa_detalle', args=[programa.id]))
    else:
        form_programa = ProgramaForm(instance=programa)

    return render(request, 'programa/programa_edit.html', {'form': form_programa})

def crear_asignacionBeneficio(request):
    nueva_asignacion = None
    if request.method == 'POST':
        programa_form = AsignacionBeneficioForm(request.POST)
        if programa_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nueva_asignacion = programa_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente la asignacion Beneficio {}'.format(nueva_asignacion))
            return redirect(reverse('programa:listar_beneficios'))
    else:
        programa_form = AsignacionBeneficioForm()

    return render(request, 'programa/programa_form.html',
                  {'form': programa_form})

#buscara por fecha de rango particular
def detalle_asignacionBeneficio(request, fecha):
    programa = get_object_or_404(AsignacionBeneficio, fecha_entrega=fecha)
    return render(request,
                  'programa/detalle_asignacionBeneficio.html',
                  {'programa': programa})

def listado_beneficios(request):
    programas = AsignacionBeneficio.objects.all()
    return render(request, 'programa/lista_beneficios.html',
                  {'programas': programas})

def crear_tipoAsistencia(request):
    if request.method == 'POST':
        programa_form = tipoAsistenciaForm(request.POST, request.FILES)
        if programa_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            programa_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el tipo de asistencia')
            return redirect(reverse('programa:listar_tipoAsistencia'))
    else:
        programa_form = tipoAsistenciaForm()

    return render(request, 'programa/crear_tipoAsistencia.html',
                  {'form': programa_form})

def lista_tipoAsistencias(request):
    programas = TipoAsistencia.objects.all()
    return render(request, 'programa/lista_tipoAsistencia.html',
                  {'programas': programas})