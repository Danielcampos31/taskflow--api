# Práctica 1.1 — Primeros endpoints y estructura inicial

## Objetivo

Crear una API inicial con FastAPI, configurar el entorno virtual y comprobar que los endpoints funcionan correctamente.

## Desarrollo

Se ha creado un entorno virtual de Python y se han instalado FastAPI y Uvicorn. El proyecto está organizado en la carpeta `app`, que contiene `__init__.py` y `main.py`.

También se ha creado `requirements.txt` para indicar las dependencias y `.gitignore` para excluir archivos innecesarios.

## Endpoints implementados

- **GET /health:** devuelve `{"status": "ok"}`.
- **GET /version:** devuelve la versión `1.0.0`.
- **GET /ping:** devuelve `{"message": "pong"}`.

Los tres endpoints incluyen `summary`, `description` y `response_model`.

## Comprobaciones

El servidor se ha iniciado con Uvicorn y se ha comprobado la documentación automática en `/docs`. Los tres endpoints se han probado desde Swagger y han respondido correctamente.

## Captura de pantalla

Se incluye una captura de la documentación Swagger donde aparecen los tres endpoints implementados.

## Conclusión

La práctica ha servido para crear la estructura inicial de una API con FastAPI, configurar las dependencias y comprobar los endpoints y la documentación automática.