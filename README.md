# Portal de Noticias Torres

Proyecto web desarrollado con Django como entrega final de la cursada de Python en CoderHouse.

## Descripción
Portal de noticias con sistema de usuarios, perfiles, mensajería interna y gestión completa de noticias con editor de texto enriquecido.

## Tecnologías utilizadas
- Python 3.13
- Django 6.0
- SQLite (base de datos por defecto de Django)
- Bootstrap 5
- CKEditor 5

## Cómo instalar y correr el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/Soletorres/TuPrimeraPagina-Torres.git
cd TuPrimeraPagina-Torres
```
    
### 2. Crear y activar el entorno virtual
```bash
python -m venv venv 
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Crear superusuario
```bash
python manage.py createsuperuser
```

### 6. Correr el servidor
```bash
python manage.py runserver
```

## Orden para probar las funcionalidades

### Registro y login
1. Entrá a **/accounts/registro/** y creá un usuario nuevo
2. O iniciá sesión en **/accounts/login/** con un usuario existente

### Noticias
3. Entrá a **Nueva Categoría** y cargá al menos una categoría (ej: Deportes)
4. Entrá a **Nuevo Autor** y cargá un autor
5. Entrá a **Nueva Noticia** y cargá una noticia con título, subtítulo, contenido y categoría
6. En el **Inicio** vas a ver la noticia publicada con el botón "Leer más"
7. Al hacer click en "Leer más" vas al detalle donde podés **Editar** o **Borrar** (solo si estás logueado)

### Búsqueda
8. Entrá a **Buscar** y buscá noticias por título

### Perfil
9. Entrá a **Mi Perfil** para ver tus datos
10. Hacé click en **Editar perfil** para modificar nombre, apellido, email, avatar y biografía
11. Desde el perfil podés también **Cambiar contraseña**

### Mensajería
12. Entrá a **📨 Mensajes** para ver tu bandeja de entrada
13. Hacé click en **Nuevo mensaje** para enviarle un mensaje a otro usuario
14. Al hacer click en un mensaje podés leerlo y responderlo

### Acerca de mí
15. Entrá a **Acerca de mí** en el navbar para ver la información del portal

### Panel de administración
16. Entrá a **/admin** con el superusuario para gestionar todos los datos

## Estructura del proyecto

## Video demostrativo
[Ver video en Google Drive](https://drive.google.com/drive/folders/11aB03awA8XWWgbKz3O1EKz57AZGVh-1q?usp=sharing)

## Autora
Soledad Torres - CoderHouse Python 2026