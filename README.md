# 03_proyectogit

https://github.com/techiediaries/django-crm/blob/master/opportunities/models.py
https://django-shop.readthedocs.io/en/latest/reference/customer-model.html
https://github.com/daniel10027/learning

https://github.com/daniel10027/D-veloppeur-d-application---Python

https://hevodata.com/learn/docker-postgresql/


# GeoDjango - Docker
# ====================

Pasos para iniciar un proyecto con geoDjango utilizando Docker dentro del flujo de trabajo. Se utiliza `projectname` para hacer referencia al nombre del projecto.

Refeencia de: https://github.com/mmorejon/docker-django

## Paso Uno - Establecer Estructura.

**_Descargar estructura del proyecto_**

Por ejemplo: Se descarga el proyecto que contiene la estructura general.
```
git clone https://github.com/antelero/03_proyectogit_geodjango projectname
```

**_Eliminar carpeta de Git_**

La carpeta `.git` se elimina para crear un nuevo repositorio.

```
cd projectname
rm -rf .git/
```

**_Crear nuevo repositorio dentro del proyecto_**

Se inicia el control de versiones dentro de la carpeta del proyecto para registrar los cambios.

```
git init
```

## Paso Dos - Crear Imagen de Docker

**_Crear Imagen en Docker_**

Se crea la imagen de Docker (DockerFile) para el projecto.
```
# syntax=docker/dockerfile:1
FROM python:3
#FROM ubuntu:jammy

ENV LANG C.UTF-8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update -qq && apt-get install -y -qq \
    # std libs
    git less nano curl \
    ca-certificates \
    wget build-essential\    
    # geodjango
    gdal-bin binutils libproj-dev libgdal-dev \
    # postgresql
    libpq-dev postgresql-client && \
    apt-get clean all && rm -rf /var/apt/lists/* && rm -rf /var/cache/apt/*

WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/

ENTRYPOINT /bin/bash
```

 La imagen va a contener la instalación de los requerimientos establecidos en el fichero `requirements.txt`.

El fichero `requirements.txt` contiene los requisitos básicos para el inicio y despliegue de una aplicación con Django, si necesita adicionarle nuevos elementos este es un buen momento.

```
docker build -t projectname:1.0 .
```

Siempre que modifique los elementos dentro del fichero `requirements.txt` tiene que repetir este paso.


**_Configurar Docker Compose_**

En el fichero `docker-compose.yml` se modifica el nombre de la imagen que será utilizada. El nombre de la imagen se ha establecido en el paso anterior. La zona que se modifica dentro del fichero es la siguiente:
```
image: projectname:1.0
```

En este proyecto se generan dos ficheros docker-compose: 
  `docker-compose.yml`    -> Utilizado para el servicio de python.
  `docker-compose_pg.yml` -> Utilizado para el servicio de Postgres/Postgis.

`docker-compose.yml`
```
services:
  web:
    image: projectname:1.0
    build: .
    command: python manage.py runserver 0.0.0.0:8000    
    volumes:
    - .:/code   
    environment:
      - POSTGRES_USER=gisuser
      - POSTGRES_PASS=password
      - POSTGRES_DB=gis
    ports:
    # - "127.0.0.1:6060:6060/udp"
      - target: 8000
        host_ip: 127.0.0.1
        published: 8000
        protocol: tcp
        mode: host
```

`docker-compose_pg.yml`
```
services:
  db:
    container_name: db
    image: kartoza/postgis:12.0
    volumes:
      - ./data/db:/var/lib/postgresql/data
    #env_file:
    #     - .env
    environment:    
      - POSTGRES_USER=gisuser
      - POSTGRES_PASS=password
      - POSTGRES_DB=gis
    ports:
      - "5432:5432"
    #psql -h 192.168.1.7 -p 5432 -d gis -U gisuser --password
```

## Paso Tres - Crear Proyecto Django

**_Crear Proyecto_**
Se crea el proyecto utilizando los mismos comandos descritos por el sitio Django.
```
docker-compose run web django-admin startproject projectname .
```

**_Probar el sistema_**
Para probar si el sistema está funcionando correctamente se ejectua el siguiente comando. En el navegador se puede revisar la aplicación en la siguiente dirección `http://<ip-máquina:8000>`. El puerto de salida puede ser configurado en el fichero `docker-compose.yml`.
```
docker-compose up
```

**_Run container and next folow next explanation_**
docker compose run web python manage.py runserver 0.0.0.0:8000


1 - Start docker and run services

2 - Start code an exect
```
docker exec -it 00_inicio_geodjango_web_run_992f94b62c2e bash
```
**_Para el sistema_**
Se detiene el sistema de ser necesario para continuar con las configuraciones.
```
Ctrl-C
```

## Paso Cuatro - Crear Aplicación

Para crear una aplicación dentro del proyecto Django se utiliza el siguiente comando:
```
docker-compose run web python manage.py startapp app
```

## Paso Cinco - Crear Usuario

Los usuarios se crean utilizando el mismo comando descrito en la documentación de Django.
```
docker-compose run web python manage.py createsuperuser
```

## Paso Seis - Entorno de Producción

Para utilizar la aplicación en el entorno de producción se debe configurar los siguientes ficheros:

Adicionar al final del fichero `projectname/settings.py` la siguiente línea:

```
STATIC_ROOT = './static/'
```

Adicionar la línea `command: ./run-production.sh` al fichero `docker-compose.yml` quedando de la siguiente forma:

```
web:
  image: projectname:1.0
  command: ./run-production.sh
  volumes:
    - .:/code
  ports:
    - "8000:80"
```

Para finalizar debe modificar el nombre del proyecto `projectname` en el fichero `conf/app.ini`.

### Enlaces relacionados con el tema

* <a target="_blank" href="https://docs.docker.com/compose/django/">Docker Compose con proyectos Django</a>
* <a target="_blank" href="https://docs.djangoproject.com/es/1.9/intro/tutorial01/">Primeros pasos en projectos con Django</a>


### Conclusiones de usar Docker con Django
Me he ahorrado la instalación de Postgresql en mi máquina.
Al compartir el proyecto, trabajaría con mis compañeros con la misma configuración lo que evitaría errores de configuración.
Es rápido, una vez aprendes a hacerlo te sirve para crear cualquier proyecto con Django.


# GeoDjango
* <a target="_blank" href="https://github.com/makinacorpus/docker-geodjango/blob/master/Dockerfile"></a>


--Ejecuta bash en un contenedor en este caso "db"
```
docker exec -it db bash
```

--Muestra los conteenedores
```
docker ps -a
```
```
docker compose run web 
```
```
docker-compose -f docker-compose.yml build --remove-orphans
```
```
docker compose run --publish 8000:8000 web bash --remove-orphans
```

