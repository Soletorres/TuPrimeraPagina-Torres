# Portal de Noticias Torres

Proyecto web desarrollado con Django como parte de la cursada de Python en CoderHouse.

## Descripción
Portal de noticias con sistema de carga y búsqueda de noticias, autores y categorías.

## Cómo correr el proyecto

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
pip install django
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Crear superusuario (para el panel admin)
```bash
python manage.py createsuperuser
```

### 6. Correr el servidor
```bash
python manage.py runserver
```

## Orden para probar las funcionalidades

1. Entrá a **Nueva Categoría** y cargá una categoría (ej: Deportes)
2. Entrá a **Nuevo Autor** y cargá un autor
3. Entrá a **Nueva Noticia** y cargá una noticia seleccionando el autor y categoría
4. En el **Inicio** vas a ver la noticia publicada
5. Entrá a **Buscar** y buscá por título de noticia
6. El panel de administración está en `/admin`

## Tecnologías usadas
- Python 3.13
- Django 6.0
- SQLite (base de datos por defecto de Django)

## Autora
Soledad Torres