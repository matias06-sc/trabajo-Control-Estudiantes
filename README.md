# Trabajo Control de Estudiantes

## 🎯 Product Backlog
Desarrollar un sistema que permita:
- Registrar estudiantes mediante un formulario web (nombre, carrera, ciclo, correo).
- Visualizar la lista de estudiantes registrados en una tabla o listado claro.
- Actualizar la información de un estudiante a través de un botón de edición.
- Eliminar registros individuales con confirmación.
- Aplicar filtros de búsqueda y parámetros para localizar estudiantes fácilmente.
- Contar con una interfaz agradable y usable, asegurando una buena experiencia visual.
- Realizar avances y pruebas en GitHub para validar el correcto funcionamiento del sistema.

## 🎯 Sprint Goal
El objetivo del sprint es desarrollar y validar un sistema de control de estudiantes con Django, implementando un CRUD completo (crear, visualizar, editar y eliminar estudiantes) desde una interfaz web, con un diseño simple, validaciones adecuadas y almacenamiento en base de datos.

## 👥 Roles Scrum
| Rol            | Integrante           | Función principal                                                                                                 |
|----------------|---------------------|------------------------------------------------------------------------------------------------------------------|
| Scrum Master   | Matias Sicha    | Facilita el proceso Scrum, elimina impedimentos y asegura que el equipo siga los principios ágiles.              |
| Product Owner  | Daniel Torres     |                         |
| Developer 1    | Rodrigo Guerra      |                                   |
| Developer 2    | Juan     |                                     |
| Developer 3    | Josue Castillo  |       |
| Developer 4    |   |   |

## 🎯 Características Principales
### ✅ **Funcionalidades CRUD**
  - Crear nuevos estudiantes con validación de datos (nombre, carrera, ciclo, correo).
  - Leer lista completa de estudiantes desde la base de datos.
  - Actualizar información de estudiantes existentes mediante formularios.
  - Eliminar estudiantes con confirmación para evitar errores.
    
### ✅ **Interfaz de Usuario**
  - Diseño simple y agradable con estilos CSS personalizados.
  - Formularios de Django para manejo de entradas y validaciones.
  - Listado dinámico de estudiantes con vistas organizadas.
  - Plantillas HTML reutilizables, garantizando coherencia en la interfaz.

### ✅ **Características Técnicas**
  - Backend: Django 4.x
  - Base de datos: SQLite (configuración por defecto).
  - Frontend: HTML + CSS personalizados.
  - Arquitectura modular con aplicación independiente para estudiantes.
  - Validación automática con formularios Django.

## 🏗️ Estructura del Proyecto

```
Proyecto Control Estudiantes/
├── control/                 # Proyecto Django principal
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Configuración del proyecto
│   ├── urls.py              # URLs principales
│   └── wsgi.py
├── estudiantes/             # Aplicación de estudiantes
│   ├── __init__.py
│   ├── admin.py             # Configuración del admin
│   ├── apps.py
│   ├── models.py            # Modelo Estudiante
│   ├── urls.py              # URLs de la app
│   ├── views.py             # Vistas y lógica
│   ├── tests.py
│   ├── migrations/          # Migraciones de la BD
│   ├── static/              # Archivos estáticos
│   │   └── Diseño/
│   │       └── estilo.css   # Estilos personalizados
│   └── templates/           # Plantillas HTML
│       └── estudiantes/
│           ├── lista.html   # Listado de estudiantes
│           └── editar.html  # Formulario editar estudiante
├── manage.py                # Script de gestión Django
├── db.sqlite3               # Base de datos SQLite
└── README.md                # Documentación
```

## 🌐 Enlace al sitio web

## Enlace del Trello
- https://trello.com/b/HN5WNBA9/django-control-de-estudiantes

## 🎥 Video explicativo (entregado por Drive):
- Nombre de la carpeta: 
- Contenido:
  - 🎥 Video
  - 📄 Documentacion:
  - 🔗 Link del Drive:


