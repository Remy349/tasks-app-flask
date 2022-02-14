# TasksApp

## Informacion de la app
Esta es un app desarrollada con Flask y Python, ademas de otras tecnologias como
Javascript para el Frontend, HTML, CSS/SASS, AJAX.

El objetivo de esta es realizar las operaaciones basicas de una aplicacion CRUD,
es decir, Crear, elminar, editar y guardar, en este caso tareas o pequeñas notas
para que el usuario pueda recordar las pequeñas tareas que debe realizar y no olvidar estas mismas.

## ¿Como funciona?
El funcionamiento es muy basico, lo que se debe realizar para iniciar es crear un nuevo usuario en caso de 
no tener uno, si ya la tienes simplemente debes iniciar sesion en tu cuenta para poder comenzar a
poder guardar tus tareas o notas, cabe recalcar que las rutas estan protegidas, por lo tanto
si no tienes un usuario e intentas visitar otras rutas, seras redirecionado al formulario de "Crear cuenta".

Una vez tienes una cuenta la app te posicionara en una vista en la cual podras ver un pequeño formulario,
en el podras crear las notas o tareas nuevas, esto se realiza de manera asincrona, por lo tanto la pagina 
no se recargara y podras ver tu nota inmediatamente en tu pantalla (mientras que en el servidor lo que escribiste 
se esta guardando en la base de datos con la que cuenta la app, esta esta hecha con SQLite).

Una vez creada la tarea aparecera en forma de tarjeta, en la parte final habran dos botones, uno para editar y el otro
para eliminar la tarea, si precionas el de editar te llevara a un formulario para cambiar el texto de lo anteriormente escrito
en ella, luego podras actualizar o cancelar si quieres mantener la misma informacion.

Y para finalizar el menu contiene un boton para cerrar tu sesion de la app.

## Ejecutar la app
Para hacer funcionar la app debes realizar lo siguiente:
1. Debes tener Python instalado en tu ordenador para poder ejecutar los siguientes comandos.
2. Si ya tienes Python ejecuta "pip install requirements.txt" y se instalaran los paquetes necesarios para
la ejecucion de esta
3. La app contiene variables de entorno, asi que deberas usar tus propias variables; estas son
"FLASK_APP=tasks" esto para que Flask encuentre el archivo que ejecutara toda la aplicacion,
tambien esta "SECRET_KEY=tuclavesecreta" en lugar de "tuclavesecreta" puedes poner la que tu quieras
esta sirve para proteger datos de usuarios y tu app, te recomiendo crear un archivo ".env" dentro del directorio 
principal y poner en el las variables ya mencionadas
4. Luego de todo esto ejecuta "flask run" y listo la app ya funcionara en el localhost:5000 de cualquier navegador.

Nota: Los campos de los formulario del inicio y registro de usuario estan validados, la app tiene responsive design,
es decir, se adapta a dispositivos mobiles. En general es una app muy basica pero la cual requirio de mucho esfuerzo de mi parte
en especial el javascript del frontend con AJAX. Puede llegar a mejorar mucho mas, se pueden agregar muchas mas funciones
pero el objetivo de su creacion es poner en practica mis conocimientos en el desarrollo web fullstack.

### Creador:
Santiago de Jesus Moraga Caldera - 2022
Desarrollador web Junior
All rights reserved!
