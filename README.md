![django](https://img.shields.io/badge/django-5.2.3-red)
![drf](https://img.shields.io/badge/drf-3.16.0-orange)

# App de Notas - Backend con Django REST Framework

Este es un backend funcional para una aplicación de notas, desarrollado con **Django** y **Django REST Framework (DRF)**. Permite a los usuarios registrarse, iniciar sesión y gestionar sus notas de forma segura.

---

## 🧾 Características

- Registro de usuarios ✅
- Autenticación por Token ✅
- CRUD de notas (Crear, Leer, Actualizar, Eliminar) ✅
- Solo los usuarios autenticados pueden acceder a sus propias notas ✅
- JSON como formato de intercambio de datos ✅

---

## 📦 Tecnologías Usadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

---

## 🚀 Cómo ejecutar el proyecto localmente

### 1. Clona el repositorio

```bash
git clone https://github.com/KingZahard01/notes-backend.git
cd notes-backend
```

### 2. Crea y activa el entorno virtual

```bash
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplica las migraciones

```bash
python manage.py migrate
```

### 5. (Opcional) Crea un superusuario

```bash
python manage.py createsuperuser
```

### 6. Inicia el servidor de desarrollo

```bash
python manage.py runserver
```

Ahora puedes acceder a la API en `http://localhost:8000/api/`.

---

## 🔐 Endpoints Disponibles

| Método    | Ruta               | Descripción                    |
| --------- | ------------------ | ------------------------------ |
| POST      | `/api/register/`   | Registrar un nuevo usuario     |
| POST      | `/api/login/`      | Iniciar sesión (obtener token) |
| GET       | `/api/notes/`      | Listar todas tus notas         |
| POST      | `/api/notes/`      | Crear una nueva nota           |
| GET       | `/api/notes/<id>/` | Leer una nota específica       |
| PUT/PATCH | `/api/notes/<id>/` | Actualizar una nota            |
| DELETE    | `/api/notes/<id>/` | Eliminar una nota              |

---

## 🧪 Pruebas

Puedes probar los endpoints usando:

- [curl](#)
- [Postman](https://www.postman.com/)
- O cualquier cliente HTTP

---

## 📁 Estructura del Proyecto

```
notes-backend/
├── core/               # Configuración general de Django
├── notes/              # App principal con modelos, vistas y serializadores
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🧪 Ejemplos de uso con `curl`

Aquí tienes algunos ejemplos prácticos de cómo usar los endpoints de la API con `curl`.

### 1. Registro de usuario

```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123",
    "email": "test@example.com"
  }'
```

### 2. Iniciar sesión y obtener token

```bash
curl -X POST http://localhost:8000/api/login/ \
  -d "username=testuser&password=testpass123"
```

Guarda el token recibido para usarlo en las siguientes peticiones.

### 3. Crear una nota

Reemplaza `YOUR_TOKEN_HERE` por el token obtenido arriba.

```bash
curl -X POST http://localhost:8000/api/notes/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Mi primera nota",
    "content": "Este es el contenido de mi nota."
  }'
```

### 4. Listar todas tus notas

```bash
curl -X GET http://localhost:8000/api/notes/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### 5. Leer una nota específica (por ID)

```bash
curl -X GET http://localhost:8000/api/notes/1/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### 6. Actualizar una nota

```bash
curl -X PUT http://localhost:8000/api/notes/1/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Nota actualizada",
    "content": "Contenido nuevo."
  }'
```

### 7. Eliminar una nota

```bash
curl -X DELETE http://localhost:8000/api/notes/1/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```
