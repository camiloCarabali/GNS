# GNS
Prueba tecnica

## Con Docker:
Si utilizas docker puedes usarlo para correr el back con el siguiente comando: `docker run -p 8000:8000 camilocarabali/api`, para correr el front simplemente usa el comando `npm i`
y comenzara a instalar todos los paquetes, en el caso de que pase un error, use el comando `npm i --force`, despues de cargar los paquetes use el comando `ng serve --open` para correr el servidor.

## Sin Docker:
Si no utilizas docker tienes que usar el comando `pip install -r requirements.txt` para tener todas las depencias del back y luego el comando `python manage.py runserver`, para
el front simplemente usa el comando `npm i` y comenzara a instalar todos los paquetes, en el caso de que pase un error, use el comando `npm i --force`, despues de cargar los paquetes use el comando `ng serve --open` para correr el servidor..
