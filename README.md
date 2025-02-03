# Despliegue de Python con Flask y Gunicorn
## Primer ejemplo
Luego de instalar los gestores de paquetes y entornos virtuales creamos el fichero oculto .env indicando cuál es el archivo .py de la aplicación y el entorno
<img src="conf-despliegue/img/entornoVirtual.png">
<a href="conf-despliegue/.env">Fichero .env</a>

Tras iniciar el entorno virtual creamos una aplicación Flsk simple con los archivos application.py, que es el que contendrá la aplicación, y el wsgi.py se encargará únicamente de iniciarla y dejarla corriendo.
<a href="conf-despliegue/application.py">Archivo application.py</a>
<a href="conf-despliegue/wsgi.py">Archivo wsgi.py</a>

Despliegue con Flask
<img src="conf-despliegue/img/appFlask.png">

Despliegue con Gunicorn
<img src="conf-despliegue/img/appGunicorn.png">


Buscamos la ruta de gunicorn
<img src="conf-despliegue/img/pathGunicorn.png">

Ya fuera de nuestro entorno virtual, crearemos un archivo para que systemd corra Gunicorn como un servicio del sistema más
<a href="conf-despliegue/rconcan.service">Archivo rconcan.service</a>

Creamos el archivo rconcan.conf en /etc/nginx/sites-available como en este ejemplo.
<a href="conf-despliegue/rconcan.conf">Archivo rconcan.conf</a>

Finalmente accedemos a la app mediante el dominio
<img src="conf-despliegue/img/rconcan-izv.png">


## Segundo ejemplo
Siguiendo los mismos pasos que en el ejemplo anterior creamos el entorno virtual de app2
<img src="conf-despliegue/img/entornoVirtual2.png">

Modificamos el archivo a <a href="conf-despliegue/application2.py">application2.py </a> para despegar la app. El archivo <a href="conf-despliegue/wsgi.py">wsgi.py</a> se mantiene igual.

Despliegue con Flask
<img src="conf-despliegue/img/flask2.png">

Despliegue con Gunicorn
<img src="conf-despliegue/img/gunicorn2.png">

Creamos el archivo para el servicio: <a href="conf-despliegue/app2.service">app2.service</a>

Luego el archivo <a href="conf-despliegue/app2.conf">app2.conf</a> para luego crear el enlace simbólico con "sudo ln -s /etc/nginx/sites-available/app2.conf /etc/nginx/sites-enabled/"

Finalmente podemos acceder a la aplicación con el dominio
<img src="conf-despliegue/img/app2-izv.png">
