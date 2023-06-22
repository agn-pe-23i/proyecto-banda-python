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
![Diagrama](https://github.com/agn-pe-23i/proyecto-banda-python/blob/main/Diagrama_estructura.png)
#Descripcion diagrama 
Para la elaboracion de este script, planteamos un diseño basandonos en el modelo top-down que consiste en establecer una serie de niveles de mayor a menor complejidad (arriba-abajo) que den solución al algoritmo.

En el caso de nuestro codigo comenzamos por la elaboracion de nuestro main en donde se ubicara el menu a partir del cual accederemos a los siguientes modulos. 

-"Agregar producto" recibe como informacion un arreglo de diccionarios y devuelve un nuevo arreglo con los datos proporcionados.

-La funcion "buscar producto" se encarga de evaluar los datos que existen dentro del arreglo de diccionarios y de existir se devuelve los productos encontrados en base al titulo. Recibe un arreglo de diccionarios y devuelve los productos obtenidos de la busqueda. 

-Para la funcion  "eliminar producto", evaluara los datos almacenados dentro del diccionario de productos. Recibe como entrada un arreglo de diccionarios y devuelve un arreglo de diccionarios sin los datos eliminados. 

-"Mostrar catalogo" es una funcion que muestra en el panel de control al usuario el catalogo disponible, puede ser de peliculas, series, documentales o eventos deportivos dependiendo de lo que solicite el usuario, tambien puede mostrar todo el catalogo. Recibe como entrada un arreglo de diccionarrios y devuelve otro a la salida en base a las palabras clave. 

-"Cargar catalogo" permite leer un archivo txt y cargarlo dentro de nuestro diccionario de resultados mostrando los elementos del archivo dentro del catalogo ya sea de series, peliculas, documentales o eventos deportivos. Devuelve como salida un arreglo de diccionarios. 

-En cuanto a la funcion "Guardar catalogo", esta permite guardar nuestro catalogo actual en un nuevo archivo txt que puede contener todos los productos que agregamos o eliminamos. Recibe como entrada un arreglo de diccionarios. 

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

#Inicializacion: El script iniciara solicitando al usuario que seleccione alguna de las opciones disponibles dentro dl menu principal utilizando valores numericos para la seleccion, de agregar otro valor entonces devolvera un valor falso; si se dirige a la opcion cargar catalogo puede subir un archivo de texto colocando el nobre del archivo seguido de .txt. Con los otros modulos puede modificar el catalogo existente o crear uno diferente.

# Comentarios 
Para comenzar con la implementacion en python, diseñamos en primer lugar el menu desde el cual el usuario podra seleccionar las opciones a las cuales desea acceder; utilizamos prints para mostrar las opciones en el panel de control y asignandoles un valor numerico y a su vez implementamos un while con el cual evaluara que el valor proporcionado por el usuario sea de tipo numerioc y se encuentre dentro del rango.

menu(): Esta función muestra el menú principal y solicita al usuario que seleccione una opción. Devuelve el número de opción seleccionada.

agregar_producto(pelicula, serie, documental, evento_deportivo): Esta función agrega un producto a la lista correspondiente. Recibe cuatro listas como parámetros: pelicula, serie, documental y evento_deportivo. Devuelve una tupla con la respuesta y las listas actualizadas. Esta funcion esta complementada a su vez por otras 4 funciones especificas para introducir un tipo de producto ya sea serie, documental, pelicula, etc y tomando el titulo como factor principal para guardar la informacion necesaria dentro de un diccionario.
Ejemplo:
agregar_evento(): Esta función solicita al usuario que ingrese los datos de un evento deportivo y devuelve un diccionario con los datos ingresados.
La función buscar_producto se encarga de buscar productos en varias listas de diccionarios (pelicula, serie, documental, evento) utilizando una palabra clave. Aquí tienes algunos comentarios sobre cómo funciona esta función:

buscar_producto: la función recibe como parámetros la palabra clave a buscar y las listas de diccionarios que contienen los productos; crea una lista vacía llamada resultados para almacenar los productos encontrados. Luego, se inicia un ciclo for para recorrer la lista de películas, dentro de este ciclo, se verifica si la palabra clave está presente en el título del diccionario o en cualquiera de sus contenidos.

Si se encuentra una coincidencia, se agrega el diccionario completo a la lista resultados utilizando el método append y se utiliza break para salir del ciclo y pasar a la siguiente lista. El mismo proceso se repite para las listas de series, documentales y eventos deportivos, utilizando ciclos for anidados para recorrer los diccionarios y verificar las coincidencias.
Finalmente, se devuelve la lista resultados que contiene todos los productos encontrados que coinciden con la palabra clave.

eliminar_producto(): Es un módulo que se encarga de eliminar un producto específico de las listas de películas, series, documentales y eventos deportivos.
La función recibe como parámetros la clave del producto a eliminar y las listas de películas, series, documentales y eventos deportivos. Llama a la función buscar_producto pasando la clave y las listas de productos como argumentos. Esto devuelve una lista llamada respuestas que contiene los productos encontrados que coinciden con la clave.

Luego llama a la función mostrar pasando respuestas como argumento, que muestra los detalles de los productos encontrados en pantalla.
Solicita al usuario una respuesta ("S" para confirmar o cualquier otra letra para cancelar) utilizando la función input.
Si la lista respuestas no está vacía y el usuario confirma la eliminación, se procede a eliminar el producto de la lista correspondiente.
Utiliza ciclos for anidados para recorrer las listas de productos y verifica si los diccionarios coinciden con los productos encontrados en respuestas. Si se encuentra una coincidencia, se utiliza el método remove para eliminar el producto completo de la lista y se muestra en pantalla un mensaje indicando que el producto ha sido eliminado del catálogo.
Si el usuario no confirma la eliminación o la lista respuestas está vacía, se devuelve o muestra un mensaje indicando que el producto no se encontró en el catálogo.
La función mostrar simplemente muestra en pantalla los títulos y contenidos de los productos contenidos en el argumento variante, que generalmente sería la lista de productos encontrados.

mostrar (variante):Se encarga de buscar productos en varias listas de diccionarios (pelicula, serie, documental, evento) utilizando una palabra clave.

regresar ciclo(): solicita al usuario si desea ingresar otro producto y devuelve True si la respuesta es "s" o False en caso contrario.

Leer archivo(): La función recibe como parámetro el nombre del archivo a leer.
Intenta abrir el archivo en modo de lectura usando open.
Lee todas las líneas del archivo y las almacena en la lista lineas.
Crea una lista vacía llamada arreglo_diccionarios donde se guardarán los productos.
Luego, itera sobre cada línea en lineas. Cada línea se divide en palabras utilizando split() y se almacena en la lista palabras.
Si la longitud de palabras es mayor o igual a 2, se toman las primeras dos palabras como el título para el diccionario utilizando join(). El resto de la línea se considera el contenido del diccionario.
Se crea un diccionario con el título y el contenido y se agrega al arreglo_diccionarios.
Finalmente, se devuelve el arreglo_diccionarios que contiene todos los productos extraídos del archivo de texto.

guardar catalogo(): Se encarga de guardar un catálogo en un archivo de texto.
La función recibe dos parámetros: arreg y nombre_archivo. arreg es el arreglo que contiene los diccionarios del catálogo, y nombre_archivo es el nombre del archivo en el cual se desea guardar el catálogo. Se utiliza el bloque with open(nombre_archivo, 'w') as archivo para abrir el archivo en modo de escritura. Esto permite escribir en el archivo y garantiza que el archivo se cerrará correctamente al finalizar.

toma un arreglo de diccionarios que representan un catálogo y guarda el contenido de cada diccionario en un archivo de texto, donde cada diccionario se representa como una oración en el archivo. Esto permite almacenar el catálogo de manera persistente para su posterior uso o consulta.

Main(): La función main es el punto de entrada principal del programa.

La función comienza inicializando varias variables, como respuesta, pelicula, serie, documental y evento_deportivo. Estas variables se utilizan para almacenar información relacionada con el catálogo. A continuación, se inicia un bucle while que se ejecuta mientras la variable respuesta sea igual a 'S'. Esto permite que el programa se ejecute continuamente hasta que el usuario decida salir.

En cada iteración del bucle, se muestra un menú principal utilizando la función menu. El usuario puede seleccionar una opción del menú ingresando un número.
Dependiendo de la opción seleccionada, se ejecutan diferentes bloques de código:

Si la opción es 1, se llama a la función agregar_producto para agregar un nuevo producto al catálogo.

Si la opción es 2, se inicia un bucle en el cual se solicitan palabras clave para buscar un producto. Luego, se llama a la función buscar_producto para realizar la búsqueda y se muestran los resultados utilizando la función mostrar.

Si la opción es 3, se inicia un bucle en el cual se solicita un título para eliminar un producto. Luego, se llama a la función eliminar_producto para eliminar el producto del catálogo.

Si la opción es 4, se muestra el catálogo completo utilizando la función mostrar. Se separa en secciones como películas, series, documentales y eventos deportivos.

Si la opción es 5, se muestra un submenú para cargar un catálogo desde un archivo. El usuario selecciona una categoría y proporciona el nombre del archivo. Luego, se llama a la función leer_archivo para leer el archivo y se guarda el contenido en el arreglo correspondiente.

Si la opción es 6, se llama a la función guardar_catalogo para guardar cada categoría del catálogo en archivos de texto separados.

Si la opción no coincide con ninguna de las anteriores, se llama a la función salir_prog para preguntar al usuario si desea salir del programa.
Después de cada bloque de código, se utiliza la función regreso_ciclo para preguntar al usuario si desea realizar otra operación dentro de esa opción del menú. Dependiendo de la respuesta, se continúa ejecutando el bucle o se sale de él.

El bucle principal sigue ejecutándose hasta que el usuario decida salir del programa. Esto se controla mediante la variable respuesta.
Finalmente, la función main se ejecuta para iniciar el programa.



