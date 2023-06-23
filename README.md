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
![Diagrama](https://github.com/agn-pe-23i/proyecto-banda-python/blob/main/Blank%20diagram.png)

# Descripcion diagrama 
Para la elaboración de este script, planteamos un diseño basándonos en el modelo top-down, que consiste en establecer una serie de niveles de mayor a menor complejidad (arriba-abajo) que den solución al algoritmo.

En el caso de nuestro código, comenzamos por la elaboración de nuestro "main", el cual se basa en primero mostrar un menú a partir del cual se tomará una decisión para saber a qué módulo acceder.

Diseñamos un menú para mostrar los siguientes módulos:

"Agregar producto": recibe como información un arreglo de arreglos de diccionarios. En este módulo se pide información acerca del producto y se agrega a un diccionario, devolviendo un nuevo arreglo con los datos proporcionados.

"Buscar producto": se encarga de evaluar los datos que existen dentro del arreglo de arreglos de diccionarios y encontrar coincidencias. Devuelve un arreglo de diccionarios con los productos encontrados basándose en palabras clave.

"Eliminar producto": evaluará los datos almacenados dentro del arreglo de arreglos de diccionarios. Recibe como entrada un arreglo de arreglos de diccionarios y devuelve un arreglo de arreglos de diccionarios. Busca coincidencias por el título o palabras clave y, de haberlas, elimina ese diccionario, devolviendo el arreglo de arreglos de diccionarios sin los datos eliminados.

"Mostrar catálogo": es una función que muestra en la pantalla el catálogo disponible, que puede ser de películas, series, documentales o eventos deportivos, dependiendo de lo que solicite el usuario. Recibe como entrada un arreglo de arreglos de diccionarios y muestra una cierta posición del arreglo según la selección.

"Cargar catálogo": permite leer un archivo .txt y cargarlo dentro de nuestro arreglo de arreglos de diccionarios, en una cierta posición del arreglo según la selección.

"Guardar catálogo": permite guardar un catálogo en especial (películas, series, etc.) en un nuevo archivo .txt que contiene todos los productos que agregamos. Recibe como entrada un arreglo de arreglos de diccionarios y guarda según una cierta posición del arreglo según la selección.

"Salir": este módulo verifica si quieres terminar el programa. Lo hace mediante una letra; si es "n", termina el programa.

# Funciones
menu(): Esta función muestra el menú principal y solicita al usuario que seleccione una opción. Devuelve el número de opción seleccionada.

agregar_producto(película, serie, documental, evento_deportivo): Esta función agrega un producto a la lista correspondiente. Recibe cuatro listas como parámetros: película, serie, documental y evento_deportivo. Devuelve una tupla con la respuesta y las listas actualizadas. Esta función está complementada a su vez por otras 4 funciones específicas para introducir un tipo de producto, ya sea serie, documental, película, etc., tomando el título como factor principal para guardar la información necesaria dentro de un diccionario.

Ejemplo:
agregar_evento(): Esta función solicita al usuario que ingrese los datos de un evento deportivo y devuelve un diccionario con los datos ingresados.

La función buscar_producto se encarga de buscar productos en varias listas de diccionarios (película, serie, documental, evento) utilizando una palabra clave. Aquí tienes algunos comentarios sobre cómo funciona esta función:

buscar_producto(): la función recibe como parámetros la palabra clave a buscar y las listas de diccionarios que contienen los productos; crea una lista vacía llamada resultados para almacenar los productos encontrados. Luego, se inicia un ciclo for para recorrer la lista de películas. Dentro de este ciclo, se verifica si la palabra clave está presente en el título del diccionario o en cualquiera de sus contenidos.

Si se encuentra una coincidencia, se agrega el diccionario completo a la lista resultados utilizando el método append y se utiliza break para salir del ciclo y pasar a la siguiente lista. El mismo proceso se repite para las listas de series, documentales y eventos deportivos, utilizando ciclos for anidados para recorrer los diccionarios y verificar las coincidencias.
Finalmente, se devuelve la lista resultados que contiene todos los productos encontrados que coinciden con la palabra clave.

eliminar_producto(): Es un módulo que se encarga de eliminar un producto específico de las listas de películas, series, documentales y eventos deportivos. La función recibe como parámetros la clave del producto a eliminar y las listas de películas, series, documentales y eventos deportivos. Llama a la función buscar_producto pasando la clave y las listas de productos como argumentos. Esto devuelve una lista llamada respuestas que contiene los productos encontrados que coinciden con la clave.

Luego llama a la función mostrar pasando respuestas como argumento, que muestra los detalles de los productos encontrados en pantalla.
Solicita al usuario una respuesta ("S" para confirmar o cualquier otra letra para cancelar) utilizando la función input.
Si la lista respuestas no está vacía y el usuario confirma la eliminación, se procede a eliminar el producto de la lista correspondiente.
Utiliza ciclos for anidados para recorrer las listas de productos y verifica si los diccionarios coinciden con los productos encontrados en respuestas. Si se encuentra una coincidencia, se utiliza el método remove para eliminar el producto completo de la lista y se muestra en pantalla un mensaje indicando que el producto ha sido eliminado del catálogo.
Si el usuario no confirma la eliminación o la lista respuestas está vacía, se devuelve o muestra un mensaje indicando que el producto no se encontró en el catálogo.

La función mostrar simplemente muestra en pantalla los títulos y contenidos de los productos contenidos en el argumento "variante", que generalmente sería la lista de productos encontrados.

"mostrar(variante)": Se encarga de buscar productos en varias listas de diccionarios (película, serie, documental, evento) utilizando una palabra clave.

regresar_ciclo(): Solicita al usuario si desea ingresar otro producto y devuelve True si la respuesta es "s" o False en caso contrario.

Leer_archivo(): La función recibe como parámetro el nombre del archivo a leer.
Intenta abrir el archivo en modo de lectura usando open.
Lee todas las líneas del archivo y las almacena en la lista "líneas".
Crea una lista vacía llamada "arreglo_diccionarios" donde se guardarán los productos.
Luego, itera sobre cada línea en "líneas". Cada línea se divide en palabras utilizando split() y se almacena en la lista "palabras".
Si la longitud de "palabras" es mayor o igual a 2, se toman las primeras dos palabras como el título para el diccionario utilizando join(). El resto de la línea se considera el contenido del diccionario.
Se crea un diccionario con el título y el contenido y se agrega al "arreglo_diccionarios".
Finalmente, se devuelve el "arreglo_diccionarios" que contiene todos los productos extraídos del archivo de texto.

guardar_catalogo(): Se encarga de guardar un catálogo en un archivo de texto.
La función recibe dos parámetros: "arreg" y "nombre_archivo". "arreg" es el arreglo que contiene los diccionarios del catálogo, y "nombre_archivo" es el nombre del archivo en el cual se desea guardar el catálogo. Se utiliza el bloque "with open(nombre_archivo, 'w') as archivo" para abrir el archivo en modo de escritura. Esto permite escribir en el archivo y garantiza que el archivo se cerrará correctamente al finalizar.

Toma un arreglo de diccionarios que representan un catálogo y guarda el contenido de cada diccionario en un archivo de texto, donde cada diccionario se representa como una oración en el archivo. Esto permite almacenar el catálogo de manera persistente para su posterior uso o consulta.

Main(): La función "main" es el punto de entrada principal del programa.

La función comienza inicializando varias variables, como "respuesta", "película", "serie", "documental" y "evento_deportivo". Estas variables se utilizan para almacenar información relacionada con el catálogo. A continuación, se inicia un bucle "while" que se ejecuta mientras la variable "respuesta" sea igual a 'S'. Esto permite que el programa se ejecute continuamente hasta que el usuario decida salir.

En cada iteración del bucle, se muestra un menú principal utilizando la función "menu". El usuario puede seleccionar una opción del menú ingresando un número.
Dependiendo de la opción seleccionada, se ejecutan diferentes bloques de código:

Si la opción es 1, se llama a la función "agregar_producto" para agregar un nuevo producto al catálogo.

Si la opción es 2, se inicia un bucle en el cual se solicitan palabras clave para buscar un producto. Luego, se llama a la función "buscar_producto" para realizar la búsqueda y se muestran los resultados utilizando la función "mostrar".

Si la opción es 3, se inicia un bucle en el cual se solicita un título para eliminar un producto. Luego, se llama a la función "eliminar_producto" para eliminar el producto del catálogo.

Si la opción es 4, se muestra el catálogo completo utilizando la función "mostrar". Se separa en secciones como películas, series, documentales y eventos deportivos.

Si la opción es 5, se muestra un submenú para cargar un catálogo desde un archivo. El usuario selecciona una categoría y proporciona el nombre del archivo. Luego, se llama a la función "leer_archivo" para leer el archivo y se guarda el contenido en el arreglo correspondiente.

Si la opción es 6, se llama a la función "guardar_catalogo" para guardar cada categoría del catálogo en archivos de texto separados.

Si la opción no coincide con ninguna de las anteriores, se llama a la función "salir_prog" para preguntar al usuario si desea salir del programa.

Después de cada bloque de código, se utiliza la función "regresar_ciclo" para preguntar al usuario si desea realizar otra operación dentro de esa opción del menú. Dependiendo de la respuesta, se continúa ejecutando el bucle o se sale de él.

El bucle principal sigue ejecutándose hasta que el usuario decida salir del programa. Esto se controla mediante la variable "respuesta".

Finalmente, la función "main" se ejecuta para iniciar el programa.

# Documentación 

#Para el correcto funcionamiento de el programa es necesario tener instalado python.

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

#Archivos txt: Para el correcto funcionamiento de este script es necesario cargar los archivos txt dentro de nuestra carpeta de python con el fin de utilizar correctamente las funciones dentro de este como lo serian "cargar catalogo". Para esto se selecciona la opcion cargar catalogo desde el menu principal del programa.

#Inicializacion: El script iniciara solicitando al usuario que seleccione alguna de las opciones disponibles dentro del menu principal utilizando valores numericos para la seleccion, de agregar otro valor entonces devolvera un valor falso;es posible agregar, eliminar o buscar un producto dentro del catalogo cargado anteriormente. Con los otros modulos puede modificar el catalogo existente o crear uno diferente.

# Comentarios sobre la implementacion y uso de modulos
Para comenzar, nos basamos en nuestro diagrama top-down para iniciar la implementación del main y llevar un control de lo que se necesitaba para la elaboración del script.

Después, implementamos un menú que nos mostrará todas las funciones disponibles del programa y nos devolverá un número; esto se hace para no complicar la comparación para el índice del menú.

Posteriormente, comenzamos con las funciones, teniendo en primer lugar "Agregar producto". Para esto, vemos que primero se requiere recuperar la información del producto, pero al ser tan diferentes entre sí, ocupamos uno para películas, otro para series, documentales, etc. Con lo anterior, creamos otro submódulo para la recuperación de datos y la creación del diccionario del producto. Después, se agrega al arreglo de arreglos y con eso termina la función.

Para la función "buscar producto", tenemos que comparar palabras clave con el título o el contenido de los diccionarios. Para ello, buscamos elemento a elemento gracias al ciclo "for". Esta función también se utiliza en la función "eliminar producto"; por ello, las palabras clave se piden fuera de la función para que se pueda utilizar, y regresa los resultados que son importantes para la función "eliminar producto" y no tanto para la función en sí.

La función "eliminar producto" está prácticamente resuelta gracias a "buscar producto"; solo se eliminan los resultados encontrados gracias a dicha función.

Para mostrar el catálogo, utilizamos el mismo proceso que en la función "buscar", ya que vamos elemento por elemento y los mostramos al usuario. La única diferencia es que se muestra un arreglo de diccionarios según la selección.

Para la función "cargar catálogo", primero necesitamos saber la estructura que tendrá el archivo para así tomar los datos e ingresarlos a un diccionario. Nuestra mejor solución es que sea por líneas, teniendo las 2 primeras palabras para el título del producto y el resto de la línea para la información del producto. Lo implementamos gracias a la función "líneas de texto" y solo tenemos que leer el archivo.

En cuanto a "guardar catálogo", es más complejo, ya que necesitamos que el archivo de texto tenga la misma estructura que los archivos que vamos a cargar. Por lo tanto, nuestra mejor solución es que cada línea del texto sea un producto. Esto lo generamos gracias a la función "líneas" de los archivos de texto.

El módulo más sencillo es "salir", pues simplemente colocamos un bucle "while" al principio del main y "salir" solo manda la condición de ruptura.
