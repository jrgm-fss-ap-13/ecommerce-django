# MyNakama - Ecommerce de Productos de Anime

## 📖 Descripción del Proyecto

**MyNakama** es una plataforma de comercio electrónico desarrollada en Django para la venta de productos relacionados con anime, específicamente mangas y figuras coleccionables. El proyecto ofrece una experiencia de compra completa con sistema de carrito de compras, gestión de usuarios, panel de administración y filtrado de productos por categorías y animes.

## ✨ Características Principales

- 🛍️ **Catálogo de Productos**: Visualización de productos organizados por categorías (mangas y figuras)
- 🔍 **Filtrado Avanzado**: Búsqueda de productos por anime específico y categoría
- 🛒 **Carrito de Compras**: Sistema completo de carrito con gestión de cantidades
- 👤 **Gestión de Usuarios**: Registro, inicio de sesión y autenticación de usuarios
- 📦 **Gestión de Inventario**: Control de stock y productos destacados
- 🎨 **Interfaz Moderna**: Diseño responsive con JavaScript y CSS personalizado
- 🔐 **Panel de Administración**: Gestión de productos y estados

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 6.0.1
- **Base de Datos**: SQLite3
- **Lenguaje**: Python 3.x
- **Dependencias Principales**:
  - `Django==6.0.1`
  - `django-autoslug==1.9.9` (para generar slugs automáticos)
  - `asgiref==3.11.0`
  - `sqlparse==0.5.5`

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)
- **Git** (opcional, para clonar el repositorio)

## 🚀 Instalación y Configuración

### Paso 1: Clonar el Repositorio (si aplica)

Si tienes el proyecto en un repositorio Git:

```bash
git clone <url-del-repositorio>
cd "ecommer-final Exponer 1"
```

### Paso 2: Crear un Entorno Virtual

Es recomendable crear un entorno virtual para aislar las dependencias del proyecto:

**Windows (PowerShell):**
```powershell
python -m venv env
```

**Windows (CMD):**
```cmd
python -m venv env
```

**Linux/Mac:**
```bash
python3 -m venv env
```

### Paso 3: Activar el Entorno Virtual

**Windows (PowerShell):**
```powershell
.\env\Scripts\Activate.ps1
```

Si encuentras problemas de permisos en PowerShell, ejecuta primero:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Windows (CMD):**
```cmd
.\env\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source env/bin/activate
```

### Paso 4: Instalar Dependencias

Una vez activado el entorno virtual, instala todas las dependencias necesarias:

```bash
pip install -r requirements.txt
```

Esto instalará automáticamente:
- Django 6.0.1
- django-autoslug 1.9.9
- Y todas las dependencias relacionadas

### Paso 5: Configurar la Base de Datos

El proyecto utiliza SQLite3 como base de datos. Ejecuta las migraciones para crear las tablas necesarias:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Paso 6: Crear un Superusuario (Opcional)

Para acceder al panel de administración de Django, crea un superusuario:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para establecer un nombre de usuario, email y contraseña.

## 🏃 Levantar el Servidor en Modo Desarrollo

Una vez completados los pasos anteriores, puedes iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

El servidor se iniciará en `http://127.0.0.1:8000/` por defecto.

### Acceder a la Aplicación

- **Página Principal**: http://127.0.0.1:8000/
- **Panel de Administración Django**: http://127.0.0.1:8000/admin/
- **Registro de Usuario**: http://127.0.0.1:8000/register/
- **Inicio de Sesión**: http://127.0.0.1:8000/accounts/login/

## 📁 Estructura del Proyecto

```
ecommer-final Exponer 1/
│
├── manage.py                 # Script de administración de Django
├── requirements.txt          # Dependencias del proyecto
├── db.sqlite3                # Base de datos SQLite
│
├── store/                    # Configuración principal del proyecto
│   ├── __init__.py
│   ├── settings.py          # Configuración de Django
│   ├── urls.py              # URLs principales
│   ├── wsgi.py              # Configuración WSGI
│   └── asgi.py              # Configuración ASGI
│
└── mynakama/                 # Aplicación principal
    ├── models.py             # Modelos de datos (Producto, Manga, Figura, etc.)
    ├── views.py              # Vistas y lógica de negocio
    ├── urls.py               # URLs de la aplicación
    ├── forms.py              # Formularios
    ├── admin.py              # Configuración del admin
    │
    ├── templates/            # Plantillas HTML
    │   ├── index.html
    │   ├── cart.html
    │   ├── info_productos.html
    │   └── ...
    │
    └── static/               # Archivos estáticos
        ├── css/              # Estilos CSS
        ├── js/               # JavaScript
        └── image/            # Imágenes
```

## 🔑 Modelos Principales

- **Anime**: Catálogo de animes disponibles
- **Producto**: Modelo base para productos
- **Manga**: Productos tipo manga (hereda de Producto)
- **Figura**: Productos tipo figura (hereda de Producto)
- **Orden**: Órdenes de compra de los usuarios
- **Carrito**: Items en el carrito de compras
- **DetalleVenta**: Detalles de las ventas realizadas

## 🎯 Funcionalidades Destacadas

### Para Usuarios:
- Navegación por productos organizados por anime
- Filtrado de productos (mangas/figuras)
- Agregar productos al carrito
- Gestión de cantidad en el carrito
- Finalizar compra
- Sistema de autenticación

### Para Administradores:
- Panel de administración de productos
- Cambiar estado de productos (activo/inactivo)
- Ordenamiento por precio y stock
- Gestión de inventario

## ⚠️ Notas Importantes

- Este proyecto está configurado para **modo desarrollo** (`DEBUG = True`)
- La base de datos SQLite se crea automáticamente al ejecutar las migraciones
- El archivo `db.sqlite3` contiene todos los datos, incluyendo productos y usuarios
- Para producción, se recomienda cambiar la `SECRET_KEY` y configurar `DEBUG = False`

## 📝 Comandos Útiles

```bash
# Crear migraciones después de cambios en modelos
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Iniciar shell de Django (para manipular datos)
python manage.py shell

# Recopilar archivos estáticos (para producción)
python manage.py collectstatic
```

## 🤝 Contribuir

Si deseas contribuir al proyecto:

1. Crea un fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Realiza tus cambios y commit (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y comercial.

## 👨‍💻 Autor

Desarrollado con Django y Python.

---

**¡Disfruta navegando y comprando productos de anime en MyNakama!** 🎌✨