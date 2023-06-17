[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LCXMIOgt)
# Proyecto
Ingeniería en Computación

Chavez Martinez Alberto
Matricula: 2223068971

Jacuinde Soria Joshua
Matricula: 2223028913

Oropeza Hernandez Bruno Gabriel
Matricula: 2223028637

Programación estructurada CB01C

# Diagrama de estructura 
![Diagrama](https://github.com/agn-pe-23i/proyecto-banda-python/blob/main/Diagrama%20de%20estructura%20.png)

Para la elaboracion de este script, planteamos un diseño basandonos en el modelo top-down que consiste en establecer una serie de niveles de mayor a menor complejidad (arriba-abajo) que den solución al algoritmo.

En el caso de nuestro codigo comenzamos por la elaboracion de nuestro main en donde se ubicara el menu a partir del cual accederemos a los siguientes modulos. Posteriormente creamos el modulo de "agregar producto" el cual tiene la funcion de recibir informacion por parte de el usuario y posteriormente almacenarla dentro de un arreglo de diccionarios en la misma funcion.

La funcion "buscar producto" se encarga de evaluar los datos que existen dentro del arreglo de diccionarios y de existir devuelve el valor buscado agregandolo a un arreglo llamado resultados, de no ser asi devuelve un valor falso.

Para la funcion  "eliminar producto", evaluara los datos almacenados dentro del diccionario de productos, solicitara al usuario ingresar el producto que desea eliminar y de existir dentro del registro procedera a eliminarlo, de no ser asi devuelve el valor falso. 

"Mostrar catalogo" es una funcion que muestra en el panel de control al usuario el catalogo disponible, puede ser de peliculas, series, documentales o eventos deportivos dependiendo de lo que solicite el usuario, tambien puede mostrar todo el catalogo.

"Cargar catalogo" permite leer un archivo txt y cargarlo dentro de nuestro diccionario de resultados mostrando los elementos del archivo dentro del catalogo ya sea de series, peliculas, documentales o eventos deportivos.

En cuanto a la funcion "Guardar catalogo", esta permite guardar nuestro catalogo actual en un nuevo archivo txt que puede contener todos los productos que agregamos o eliminamos.

# Documentación 

#Funcion del script: Permite crear catalogos y modificarlos ya sea agregando o eliminando productos asi como mostrando lo que existe dentro del catalogo; en este caso especifico se utilizo para desarrollar el catalogo dentro de una plataforma de streaming.

#Librerias: Las librerías os y time en Python son utilizadas para realizar diferentes tareas relacionadas con el sistema operativo y el manejo del tiempo, respectivamente. Aquí tienes una descripción de cada una de ellas:

os: La librería os proporciona una interfaz para interactuar con el sistema operativo subyacente. Permite realizar tareas como:

Acceder a variables de entorno del sistema.
Manipular rutas de archivos y directorios.
Ejecutar comandos del sistema operativo.
Crear, eliminar y modificar directorios y archivos.
Cambiar el directorio de trabajo actual.
Obtener información sobre el sistema operativo, como el tipo de sistema, el nombre del usuario, etc.
En resumen, la librería os es útil cuando necesitas interactuar con el sistema de archivos, ejecutar comandos del sistema o acceder a variables de entorno.

time: La librería time proporciona funciones para trabajar con el tiempo y la fecha. Algunas de las funcionalidades que ofrece incluyen:

Obtener la hora y la fecha actual.
Convertir entre diferentes representaciones de tiempo (timestamps, estructuras de tiempo, cadenas de texto, etc.).
Pausar la ejecución de un programa durante un cierto intervalo de tiempo.
Medir el tiempo de ejecución de un bloque de código.
En resumen, la librería time es útil cuando necesitas realizar operaciones relacionadas con el tiempo, como medir la duración de una tarea, programar eventos o realizar operaciones de sincronización.

#Archivos txt: Para el correcto funcionamiento de este script es necesario cargar los archivos txt dentro de nuestra carpeta de python con el fin de utilizar correctamente las funciones dentro de este como lo serian "cargar catalogo" 

#Inicializacion: El script iciiara solicitando al usuario que seleccione alguna de las opciones disponibles dentro dl menu principal utilizando valores numericos para la seleccion, de agregar otro valor entonces devolvera un valor falso; si se dirige a la opcion cargar catalogo puede subir un archivo de texto colocando el nobre del archivo seguido de .txt. Con los otros modulos puede modificar el catalogo existente o crear uno diferente.

# Comentarios 
Para comenzar con la implementacion en python, diseñamos en primer lugar el menu desde el cual el usuario podra seleccionarr las opciones a las cuales desea acceder; utilizamos prints para mostrar las opciones en el panel de control y asignandoles un valor numerico y a su vez implementamos un while con el cual evaluara que el valor proporcionado por el usuario sea de tipo numerioc y se encuentre dentro del rango.

"def agregar_producto" si el usuario selecciona la opcion numero 2 desde el menu principal es dirigido a la funcion de agregar producto, se le solicitara al usuario seleccionar el tipo de producto que desea agregar.
