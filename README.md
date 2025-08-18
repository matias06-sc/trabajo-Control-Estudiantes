# Trabajo Control de Estudiantes
Sistema web desarrollado con Django que permite la gestión de estudiantes, implementando un CRUD completo (crear, visualizar, actualizar y eliminar), con almacenamiento en base de datos y una interfaz sencilla basada en HTML y CSS.

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
| Rol            | Integrante           | Función principal                                                                                                                         |
|----------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Scrum Master   | Matias Sicha    | Facilita el proceso Scrum, elimina impedimentos y asegura que el equipo siga los principios ágiles.              |
| Product Owner / Developer 1  | Daniel Torres     | Desarrolla la estructura de las plantillas HTML para la interfaz de usuario.                        |
| Developer 2    | Rodrigo Guerra      |  Desarrolla e implementa las funciones necesarias del sistema, enfocándose en la lógica de las operaciones y la interacción entre los módulos.   |
| Developer 3    | Juan Solis    | Implementa pruebas automatizadas bajo metodología TDD y desarrolla parte de la lógica del CRUD; además, participa en pair programming junto a Kevin.  |
| Developer 4    | Josue Castillo  | Se encarga del desarrollo de la parte frontend en el proyecto, integrando la interfaz de usuario con los estilos y asegurando una experiencia fluida.      |
| Developer 5    | Kevin Yupanqui  | Apoya en la construcción de pruebas TDD junto a Juan, colabora en la integración de módulos y participa en pair programming para mejorar la calidad del código.  |

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
- Nombre de la carpeta: Proyecto-control-de-estudiantes
- Contenido:
  - 🎥 Video
  - 📄 Documentacion
  - 🔗 Link del Drive: https://drive.google.com/file/d/1kgCy2CoxxvS8mY_PhN2RqS5VCB6n5ihC/view?usp=sharing
 
## 🚀 Instalación y Configuración

### 1. **Clonar el repositorio**
```bash
git clone <URL_DEL_REPOSITORIO>
cd trabajo-Control-Estudiantes
```

### 2. **Crear entorno virtual**
```bash
python -m venv venv
```

### 3. **Activar entorno virtual**
```bash
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 4. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

### 5. **Configurar la base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. **Ejecutar el servidor**
```bash
python manage.py runserver
```

## 📝 Historias de Usuario y Criterios de Aceptación

📌 **HU-01: Registrar Estudiante**

Historia: Registrar nuevos estudiantes para mantener la base de datos actualizada.

**Criterios de aceptacion:**
  - Guardar registros en la base de datos.
  - Visualizar el nuevo estudiante en la lista.
  - Formulario con nombre, carrera, ciclo y correo.

📌 **HU-02: Ver Estudiantes**

Historia: Consultar la lista de estudiantes registrados.

**Criterios de aceptacion:**
  - Mostrar tabla con todos los registros.
  - Ordenar alfabéticamente.

📌 **HU-03: Editar Estudiantes**

Historia: Actualizar datos de un estudiante.

**Criterios de aceptacion:**
  - Opción de modificar en cada registro.
  - Guardar cambios en la base.
  - Mostrar error si hay datos inválidos.

📌 **HU-04: Eliminar Estudiantes**

Historia: Borrar estudiantes innecesarios.

**Criterios de aceptacion:**
  - Botón de eliminar en la tabla.
  - Eliminación directa del registro.

📌 **HU-05: Filtrar Estudiantes**

Historia: Buscar registros de forma rápida.

**Criterios de aceptacion:**
  - Campo de texto para nombre.
  - Combobox para carrera y ciclo.
  - Botón de filtrar.

📌 **HU-06: Interfaz Agradable**

Historia: Usar un diseño claro y entendible.

**Criterios de aceptacion:**
  - Texto legible.
  - Filas de tabla alternadas en blanco y gris.
  - Botones con colores llamativos.


