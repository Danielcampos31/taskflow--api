# TaskFlow API

## Descripción

TaskFlow API es un proyecto inicial desarrollado con FastAPI para aprender a crear una API web y comprobar su funcionamiento mediante endpoints.

## Estructura del proyecto

- `app/__init__.py`: identifica `app` como un paquete de Python.
- `app/main.py`: contiene la aplicación y los endpoints.
- `requirements.txt`: indica las dependencias necesarias.
- `.gitignore`: excluye archivos que no deben subirse al repositorio.

## Endpoints

- `GET /health`: devuelve `{"status": "ok"}` para comprobar el estado de la API.
- `GET /version`: devuelve la versión actual.
- `GET /ping`: devuelve `{"message": "pong"}` para comprobar que responde.

Los endpoints incluyen resumen, descripción y modelo de respuesta para facilitar su documentación automática.

## Instalación y ejecución

1. Crear y activar un entorno virtual.
2. Instalar las dependencias con `python -m pip install -r requirements.txt`.
3. Arrancar el servidor con `python -m uvicorn app.main:app --reload`.
4. Abrir `http://127.0.0.1:8000/docs` para consultar la documentación.

## Decisiones tomadas

Se utiliza FastAPI por su sencillez y porque genera documentación automática. Uvicorn ejecuta el servidor. El entorno virtual mantiene las dependencias separadas de las del sistema y `requirements.txt` permite instalarlas de nuevo.

## Limitaciones

Esta versión solo incluye endpoints de comprobación. Todavía no permite gestionar tareas reales.