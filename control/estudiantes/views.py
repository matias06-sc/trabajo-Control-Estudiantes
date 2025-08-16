from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError   # 👈 importa esto
from .models import Estudiante

# Lista todos los estudiantes
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista.html', {'estudiantes': estudiantes})

# Crear un estudiante
def crear_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        carrera = request.POST['carrera']
        ciclo = request.POST['ciclo']
        correo = request.POST['correo']

        try:
            Estudiante.objects.create(
                nombre=nombre,
                carrera=carrera,
                ciclo=ciclo,
                correo=correo
            )
            return redirect('lista_estudiantes')
        except IntegrityError:
            estudiantes = Estudiante.objects.all()
            return render(request, 'estudiantes/lista.html', {
                'estudiantes': estudiantes,
                'error': f"El correo {correo} ya está registrado."
            })

    return render(request, 'estudiantes/lista.html', {
        'estudiantes': Estudiante.objects.all()
    })

# Editar estudiante
def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.nombre = request.POST['nombre']
        estudiante.carrera = request.POST['carrera']
        estudiante.ciclo = request.POST['ciclo']
        estudiante.correo = request.POST['correo']
        try:
            estudiante.save()
            return redirect('lista_estudiantes')
        except IntegrityError:
            estudiantes = Estudiante.objects.all()
            return render(request, 'estudiantes/lista.html', {
                'estudiantes': estudiantes,
                'estudiante': estudiante,
                'error': f"El correo {estudiante.correo} ya está registrado."
            })
    return render(request, 'estudiantes/editar.html', {'estudiante': estudiante})

# Eliminar estudiante
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('lista_estudiantes')
