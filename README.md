# WEB ICF

Inicio de página web para la carrera de ingeniería civil informática UNAB.

### Techs

Esta aplicacion emplea el uso de distintas herramientas para su correcto funcionamiento:

* [Python3](https://www.python.org/) Python!
* [Django](https://www.djangoproject.com/) - Python Web Framework
* [DjangoRestFramework](https://www.django-rest-framework.org/) - Python toolkit para web APIs
* [Tweepy](https://github.com/tweepy/tweepy) - Python API de Twitter
* [Docker](https://www.docker.com/) Contenedor de aplicaciones :)

### Instalación

La presente página requiere de [Python](https://www.python.org/) v3.5+ y [Docker-compose](https://docs.docker.com/compose/) para ser ejecutada.

Instale Docker y docker-compose para ejecutar la imágen:
```bash
$ cd /tmp
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sh get-docker.sh
$ sudo usermod -aG docker $USER
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ reboot
$ cd {PATH_TO_THIS_PROJECT}
$ docker-compose up -d
```

O bien, solo instale Django y las dependencias del proyecto para iniciar el servidor:
```bash
$ pip install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver 0:8080
```
