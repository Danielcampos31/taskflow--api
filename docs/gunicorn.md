# Instalación básica de Gunicorn

## 1. Objetivo

El objetivo de esta práctica es ejecutar la API TaskFlow utilizando Gunicorn y comprobar que sus endpoints funcionan correctamente.

## 2. Instalación y configuración

Se ha utilizado Python 3.13.6 y un entorno virtual para instalar las dependencias del proyecto sin afectar al sistema.

Se ha creado el archivo `requirements.txt` con las dependencias necesarias:

- FastAPI
- Uvicorn
- Gunicorn

Las dependencias se han instalado con:

```bash
python -m pip install -r requirements.txt
```

## 3. Arranque de Gunicorn

Para iniciar la aplicación se utiliza el siguiente comando:

```bash
gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker --bind 127.0.0.1:8000
```

- `gunicorn`: inicia el servidor de aplicaciones.
- `app.main:app`: indica dónde se encuentra la aplicación FastAPI.
- `--worker-class uvicorn.workers.UvicornWorker`: permite que Gunicorn ejecute una aplicación ASGI, como FastAPI.
- `--bind 127.0.0.1:8000`: escucha únicamente en la dirección local, en el puerto 8000.

Se utiliza `UvicornWorker` porque FastAPI trabaja con ASGI, mientras que Gunicorn necesita un trabajador compatible para ejecutar la aplicación.

## 4. Comprobación de los endpoints

Con Gunicorn en funcionamiento, se han realizado las siguientes pruebas:

```bash
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/version
curl -i http://127.0.0.1:8000/ping
```

Las tres peticiones han respondido correctamente con el código HTTP 200 y datos en formato JSON.

## 5. Servidor web y servidor de aplicaciones

Apache es un servidor web que recibe peticiones HTTP y puede servir contenido estático o actuar como intermediario hacia una aplicación.

Gunicorn es un servidor de aplicaciones que ejecuta código Python y puede utilizar varios trabajadores para atender peticiones.

En un despliegue real, Apache puede recibir las peticiones externas y reenviarlas a Gunicorn.

## 6. Dirección de escucha

La opción `--bind` indica la dirección IP y el puerto donde escucha Gunicorn.

- `127.0.0.1:8000`: permite acceder desde la propia máquina.
- `0.0.0.0:8000`: permite escuchar en todas las interfaces de red disponibles.

En esta práctica se utiliza `127.0.0.1` para limitar el acceso a la propia máquina y evitar exponer directamente el servidor en la red.

## 7. Iniciar y detener el servidor

Para iniciar el servidor, se activa el entorno virtual y se ejecuta el comando de Gunicorn indicado anteriormente.

Para detenerlo, se pulsa `Ctrl + C` en la terminal donde está ejecutándose.

## 8. Problemas habituales

- Si aparece un error de módulo, hay que comprobar que las dependencias estén instaladas en el entorno virtual.
- Si el puerto está ocupado, hay que comprobar si otro proceso está utilizando el puerto 8000.
- Si las peticiones no funcionan, hay que verificar que Gunicorn esté iniciado y que la dirección y el puerto sean correctos.

## 9. Conclusión

Se ha instalado Gunicorn, se ha ejecutado la API TaskFlow y se han comprobado los endpoints `/health`, `/version` y `/ping`. Las pruebas han finalizado correctamente.
