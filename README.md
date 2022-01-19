# Backend_reservas

El presente codigo permite al usuario crear, ver, editar o eliminar las reservas realizadas y al mismo tiempo gestionar los planes que se ofrecen a los clientes.

Lo primero por hacer es clonar el repositorio en la carpeta del backend_reservas:
```sh
$ git clone https://github.com/Cat-cafe-page/backend_reservas.git
```
Luego se instalan las dependencias:
```sh
(env)$ pip3 install -r requirements.txt
```
Una vez `pip` ha terminado de instalar las dependencias cree la base de datos en postgreSQL, modifique los datos de la base de datos en el settings y luego corra el proyecto en su maquina local:
```sh
(env)$ python manage.py runserver
```
y navega a: `http://localhost:8000/`
