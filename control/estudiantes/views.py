from django.shortcuts import render, redirect, get_object_or_404
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
        Estudiante.objects.create(nombre=nombre, carrera=carrera, ciclo=ciclo, correo=correo)
        return redirect('lista_estudiantes')
    return render(request, 'estudiantes/lista.html')   # 👈 corregido

# Editar estudiante
def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.nombre = request.POST['nombre']
        estudiante.carrera = request.POST['carrera']
        estudiante.ciclo = request.POST['ciclo']
        estudiante.correo = request.POST['correo']
        estudiante.save()
        return redirect('lista_estudiantes')
    return render(request, 'estudiantes/lista.html', {'estudiante': estudiante})

# Eliminar estudiante
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('lista_estudiantes')
