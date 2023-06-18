import os 
import time #Librería.


def agregar_producto(pelicula, serie, documental, evento_deportivo):  #Módulo para agregar producto.
    respuesta_2 = 'S'
    respuesta = 'S'
    a = True
    while respuesta_2 == 'S':
        os.system('cls')
        print('Agregar Producto'.center(100, ' '))
        print('Seleccione la opcion deseada'.center(100, ' '))
        print('='.center(100, '='))
        print('1.- Agregar Pelicula.')            #Mostramos las opciones en pantalla.
        print('2.- Agregar Serie.')
        print('3.- Agregar Documental.')
        print('4.- Agregar Evento deportivo.')
        print('5.- Salir.')
        while True:  #Ciclo para generar agregado.
            respuesta_2 = input('Ingrese la opcion deseada\n')  #Pedimos que ingrese el número de la opción deseada.
            if respuesta_2.isdigit() and (1 <= int(respuesta_2) <= 5):  #Condición para que verifique que el número ingresado sea dígito y tiene que estar dentro de los valores.
                respuesta_2 = int(respuesta_2)  
                if respuesta_2 == 1:  #Si la respuesta es 1.
                    while a:  #Mientras "a" tenga "S" se agregaran más productos.
                        pelicula.append(agregar_peli())  #Agregara los datos de la película a la lista.
                        a = regreso_ciclo()  #Se pregunta si se quiere agregar otro producto.
                    break
                elif respuesta_2 == 2:  #Si la respuesta es 2.
                    while a:  #Mientras "a" tenga "S" se agregaran más productos.
                        serie.append(agregar_serie())  #Agregara los datos de la serie a la lista.
                        a = regreso_ciclo()  #Se pregunta si se quiere agregar otro producto.
                    break
                elif respuesta_2 == 3:  #Si la respuesta es 3.
                    while a:  #Mientras "a" tenga "S" se agregaran más productos.
                        documental.append(agregar_documental())  #Agregara los datos del documental a la lista.
                        a = regreso_ciclo()  #Se pregunta si se quiere agregar otro producto.
                    break
                elif respuesta_2 == 4:  #Si la respuesta es 4.
                    while a:  #Mientras "a" tenga "S" se agregaran más productos.
                        evento_deportivo.append(agregar_evento())  #Agregara los datos del documental a la lista.
                        a = regreso_ciclo()  #Se pregunta si se quiere agregar otro producto.
                    break
                elif respuesta_2 == 5:  #Si la respuesta es 5
                    respuesta = 'S'  #Para seguir dentro del programa principal.
                    respuesta_2 = 'N'  #Dara la opción de salir o del modulo.
                    break
                else:
                    print('No es un caracter valido.')  #Si la respuesta es alguna otra letra, no será válido.
                    continue
            else:
                print('No es un numero.')  #Si la respuesta no es un número no lo hara válido.
                continue
    return respuesta, pelicula, serie, documental, evento_deportivo  #Devuelbe respuesta, pelicula, serie, documental y evento_deportivo.

def agregar_evento():  #Módulo para agregar evento deportivo.
    print('Evento deportivo'.center(100, ' '))
    titulo = input('Ingresa el título del evento deportivo\n')  
    deporte = input('Ingresa deporte del que trata.\n')  
    fecha = input('Ingresa la fecha de transmisión\n')        #Pedimos que ingrese los datos solicitados del evento deportivo.
    hora = input('Ingresa la hora de transmisión.\n')  
    lugar = input('Ingresa el lugar de donde se lleva acabo.\n')  
    evento = {titulo: 'Deporte: ' + deporte + ' Año de lanzamiento: ' + fecha + ' Hora de transmicion: ' + hora
                      + ' Lugar: ' + lugar}  #Variable que contiene el diccionario que se agrega al arreglo.
    return evento  #Devuelve evento.

def agregar_documental():  #Módulo para agregar documental.
    print('Documental'.center(100, ' '))
    titulo = input('Ingresa el título del documental\n') 
    tema = input('Ingresa el tema del documental\n')  
    director = input('Ingresa el director o directora del documental\n')    #Pedimos que ingrese los datos solicitados del documental.
    fecha = input('Ingresa el año de lanzamiento del documental\n')  
    documental = {titulo: 'Tema: ' + tema + ' Director: ' + director + ' Año lanzamiento: ' + fecha}  #Variable que contiene el diccionario que se agrega al arreglo. 
    return documental  #Devuelve documental.

def agregar_serie():  #Módulo para agregar serie.
    print('Serie'.center(100, ' '))  
    titulo = input('Ingresa el título de la serie\n')  
    actor = input('Ingresa el actor o actora principal de la serie\n')  
    director = input('Ingresa el director o directora de la serie\n')     #Pedimos que ingrese los datos solicitados de la serie.
    temporadas = input('Ingresa las temporadas de la serie\n')  
    serie = {titulo: 'Actor pricipal: ' + actor + ' Temporadas: ' + temporadas + ' Director: ' + director}  #Variable que contiene el diccionario que se agrega al arreglo.
    return serie  #Devuelve serie.

def agregar_peli():  #Módulo para agregar película.
    print('Pelicula'.center(100, ' '))
    titulo = input('Ingresa el título de la pelicula.\n')  
    actor = input('Ingresa el actor o actora principal de la película.\n')  
    fecha = input('Ingresa el año de lanzamiento de la pelicula.\n')        #Pedimos que ingrese los datos solicitados de la película.
    director = input('Ingresa el director o directora de la pelicula.\n')  
    peli = {titulo: 'Actor principal: ' + actor + ' Año de lanzamiento: ' + fecha + ' Director: ' + director}  #Variable que contiene el diccionario que se agrega al arreglo.
    return peli  #Devuelve peli.


def regreso_ciclo():  #Módulo para agregar otro producto.
    respuesta_2 = input('¿Quiere ingresar otro? [S/otra letra].\n')  #Preguntamos si se desea ingregar otro producto.
    if respuesta_2.isalpha() and respuesta_2.lower() == 's':  #Si la respuesta es "s"
        respuesta_2 = True                                    #entonces se repite el ciclo while.
    else:
        respuesta_2 = False  #Si la respuesta es cualquier letra, se rompre el ciclo.
    return respuesta_2  #Devolver respuesta_2.


def buscar_producto(palabras_clave, pelicula, serie, documental, evento):  #Módulo para buscar producto.
    resultados = []  #Lista para guardar los resultados encontrados.
    for producto in pelicula:  #Ciclo para buscar el "producto" en el arreglo película.
        if palabras_clave in producto:  #Si las palabras clave se encuentran en los títulos del diccionario.
            resultados.append(producto)  #Entonces agregara todos los datos del diccionario al arreglo "resultados".
            break
        for i_2 in producto:
            if palabras_clave in i_2:       #Si se encuentra dentro del contenido de los diccionario.
                resultados.append(producto)  #Entonces agregara todos los datos del diccionario al arreglo "resultados".
                break
            for i_3 in producto[i_2]:
                if palabras_clave in i_3:       #Si se encuentra dentro del contenido de los diccionario.
                    resultados.append(producto)  #Entonces agregara todos los datos del diccionario al arreglo "resultados".
                    break
    for producto in serie:   #Ciclo para buscar el "producto" en el arreglo serie.
        if palabras_clave in producto:   #Si las palabras clave se encuentran en los títulos del diccionario.
            resultados.append(producto)  #Entonces agregara todos los datos del diccionario al arreglo "resultados".
            break
        for i_2 in producto:
            if palabras_clave in i_2:        #Si se encuentra dentro del contenido de los diccionario.
                resultados.append(producto)  #Entonces agregara todos los datos del diccionario al arreglo "resultados".
                break
            for i_3 in producto[i_2]:
                if palabras_clave in i_3:        #Si se encuentra dentro del contenido de los diccionario.
                    resultados.append(producto)  #Entonces agregara todos los datos del diccionario al arreglo "resultados".
                    break
    for producto in documental:  #Ciclo para buscar el "producto" en documental
        if palabras_clave in producto:  #Si las palabras clave se encuentran en producto.
            resultados.append(producto)  #Entonces agregara todos los datos del documental a la lista.
            break
        for i_2 in producto:
            if palabras_clave in i_2:       #Si se encuentra dentro del contenido de los diccionario.
                resultados.append(producto)  #Entonces agregara todos los datos del diccionario al arreglo "resultados".
                break
            for i_3 in producto[i_2]:
                if palabras_clave in i_3:       #Si se encuentra dentro del contenido de los diccionario.
                    resultados.append(producto)  #Entonces agregara todos los datos del diccionario al arreglo "resultados".
                    break
    for producto in evento:   #Ciclo para buscar el "producto" en el arreglo evento.
        if palabras_clave in producto:  #Si las palabras clave se encuentran en los títulos del diccionario.
            resultados.append(producto) #Entonces agregara todos los datos del diccionario al arreglo "resultados".
            break
        for i_2 in producto:
            if palabras_clave in i_2:       #Si se encuentra dentro del contenido de los diccionario.
                resultados.append(producto)  #Entonces agregara todos los datos del diccionario al arreglo "resultados".
                break 
            for i_3 in producto[i_2]:
                if palabras_clave in i_3:       #Si se encuentra dentro del contenido de los diccionario.
                    resultados.append(producto)  #Entonces agregara todos los datos del diccionario al arreglo "resultados".
                    break
    return resultados  #Devuelve resultados.


def eliminar_producto(clave, pelicula, serie, documental, evento_deportivo):  #Módulo para elminiar producto.
    respuestas = buscar_producto(clave, pelicula, serie, documental, evento_deportivo)  #Busca el porducto específico y lo agrega a "respuesta".
    mostrar(respuestas)  #Te muestra el producto a eliminar.
    respuesta = input('¿Seguro quieres eliminarlo? [S/otra letra]\n').upper()  #Preguntamos si está seguro de eliminar el producto.
    if respuestas:
        if respuesta == 'S':  #Si la reespuesta es "s".
            for i in pelicula:                    #Buscara elemento en "película".
                if [i] == respuestas:             #Si el diccionario coincide con "respuestas"
                    pelicula.remove(i)            #eliminara el producto entero.
                    print(f"Producto' {clave} 'eliminado del catálogo.")  #Mostramos en pantalla que la película fue eliminada del catálogo.
                    break
                else:
                    for i_1 in serie:               #Buscara elemento en "serie".
                        if [i_1] == respuestas:     #Si el diccionario coincide con "respuestas"
                            serie.remove(i_1)       #eliminara el producto entero.
                            print(f"Producto' {clave} 'eliminado del catálogo.")  #Mostramos en pantalla que la serie fue eliminada del catálogo.
                            break
                        else:
                            for i_2 in documental:             #Buscara elemento en "documental".
                                if [i_2] == respuestas:        #Si el diccionario coincide con "respuestas"
                                    documental.remove(i_2)     #eliminara el producto entero.
                                    print(f"Producto' {clave} 'eliminado del catálogo.")  #Mostramos en pantalla que el documental fue eliminado del catálogo.
                                    break
                                else:
                                    for i_3 in evento_deportivo:            #Buscara elemento en "evento_deportivo".
                                        if [i_3] == respuestas:             #Si el diccionario coincide con "respuestas"
                                            evento_deportivo.remove(i_3)    #eliminara el producto entero.
                                            print(f"Producto' {clave} 'eliminado del catálogo.")  #Mostramos en pantalla que el evento fue eliminado del catálogo.
                                            break
        else:
            return  #Regresa.
    else:
        print(f"No se encontro el producto '  {clave}  'en el catálogo.")  #Si el título que desea elimnar no se encuentra en general
                                                                           #dirá que no se encontró el producto.

def mostrar(variante):  #Módulo para mostrar catálogo.
    for i in variante:  #"Variente" obtentra el arreglo a ocupar.
        for i_2 in i:        #Pedimos que muestre el título del diccionario
            print(i_2)       #y el contenido del título del diccionario.
            print(i[i_2])    #Y que pase al siguiente por el ciclo.
    return  #Regresa.


def leer_archivo(nombre_archivo):  #Módulo para leer archivos de texto.
    try:  # Para ver si el archivo existe.
        with open(nombre_archivo, 'r') as archivo:  # Se abre el archivo solamente para lectura.
            lineas = archivo.readlines()  # Cada línea del texto se almacena en "lineas".
        arreglo_diccionarios = []  # Arreglo donde se guardaran los productos.
        for linea in lineas: # Para ir línea por línea del texto.
            palabras = linea.strip().split()  # Separa cada línea en palabras
            if len(palabras) >= 2:
                clave = ' '.join(palabras[:2])                # Toma las primeras dos palabras como el título para el diccionario.
                diccionario = {clave: ' '.join(palabras[2:])} # Crea un diccionario con el título de antes y el resto de la línea es su contenido.
                arreglo_diccionarios.append(diccionario)      # Agrega el diccionario al arreglo.
        return arreglo_diccionarios  # Devuelve el arreglo
    except FileNotFoundError: # Si no existe el arichivo.
        arreglo_diccionarios = [] # Deja vacio el arreglo.
        print("El archivo no fue encontrado.") # Muestra que no se encontro el archivo.
        return arreglo_diccionarios  #Devolver arreglo_diccionarios.


def guardar_catalogo(arreg, nombre_archivo):  #Módulo para guardar catálogo.
    with open(nombre_archivo, 'w') as archivo:  #Crea un archivo de texto.
        for diccionario in arreg:  #Va de diccionar en diccionaro en el arreglo en turno.
            oracion = ' '.join([f"{clave}: {valor}" for clave, valor in diccionario.items()])  #Hace que cada oración del texto sea el contenido del diccionario.
            archivo.write(oracion + '\n') #Da un salto de línea en el texto.


def salir_prog():  #Módulo para salir del programa.
    while True:  #Ciclo para confirmar.
        respuesta = input('¿Seguro quieres salir?  [S/N]\n')  #Preguntamos si se desea salir del programa.
        if respuesta.isalpha():  #Verificamos que sea una letra.
            if respuesta.lower() == 's':  #Comparamos que sea "s".
                respuesta = 'N'           #De serlo la respuesta cambiara a "N"
                break                     #para cerrar el programa principal.
            elif respuesta.lower() == 'n':  #Comparamos que sea "n".
                respuesta = 'S'             #De serlo la respuesta cambiara a "S"
                break                       #para permanecer en el programa principal.
            else:
                print('No es un caracter valido.')  #Si la respuesta es alguna otra letra, no será válido.
                continue
        else:
            print('No es una letra.')  #Si la respuesta es un número, no será válido.
            continue
    return respuesta  #Devuelve respuesta


def menu():  #Módulo del menú principal.
    print('Menu Principal'.center(100, ' '))
    print('Seleccione la opcion deseada'.center(100, ' '))
    print('='.center(100, '='))                              
    print('1.- Agregar Producto.')                           
    print('2.- Buscar Producto.')                            
    print('3.- Eliminar Producto.')    #Mostramos todas las opciones del menú en pantalla.
    print('4.- Mostrar Catálogo.')
    print('5.- Cargar Catálogo.')
    print('6.- Guardar Catálogo.')
    print('7.- Salir.')
    while True:  #Ciclo para comprobar.
        respuesta_menu = input('Ingrese el numero de opcion que desea:\n')  #Pedimos que ingrese el número de la opción deseada.
        if respuesta_menu.isdigit() and (1 <= int(respuesta_menu) <= 7):  #Condición para que verifique que el número ingresado sea dígito y tiene que estar dentro de los valores.
            respuesta_menu = int(respuesta_menu)  
            break
        else:  #Si la condición anterior no se cumple, nos mostrara un mensaje en pantalla.
            print('No es valido.')
            continue
    return respuesta_menu  #Devolver respuesta


def main():  #Módulo main
    respuesta = 'S'  #Inicializa para que se ejecute al menos una vez.
    pelicula = []  #Lista para las películas.
    serie = []  #Lista para las series.
    documental = []  #Lista para los docuemntales.
    evento_deportivo = []  #Lista para los eventos deportivos.
    while respuesta == 'S':  #Miestras sea "S" va a seguir ejecutando en programa.
        a = True  
        a_1 = True        #Se inicializan variables para que se ejecuten al menos una vez.
        a_2 = True
        os.system('cls')
        indice_menu = menu()  #Se muestra el menú principal.
        if indice_menu == 1:  #Si es 1 se agrega un producto.
            respuesta, pelicula, serie, documental, evento_deportivo = agregar_producto(pelicula, serie, \
                                                                                        documental, evento_deportivo)
        elif indice_menu == 2:  #Si es 2.
            while a_1:
                palabras_clave = input("Ingrese palabras clave para buscar un producto: \n")  #Se piden las palabras clave.
                resultados = buscar_producto(palabras_clave, pelicula, serie, documental, evento_deportivo)  #Se busca producto.
                if resultados:
                    print("Resultados encontrados:", '\n')  #Se muestra que se encontro resultados y los muestra.
                    mostrar(resultados)
                else:
                    print("No se encontraron productos con las palabras clave proporcionadas.")  #Se muestra que no se encontraron resultados.
                a_1 = regreso_ciclo()  #Preguntamos si quiere buscar otro producto.
        elif indice_menu == 3:  #Si es 3.
            while a_2:
                titulo = input('Ingresa el titulo que quieres eliminar.\n')  #Se pide el título a eliminar.
                eliminar_producto(titulo, pelicula, serie, documental, evento_deportivo)  #Se elimina.
                a_2 = regreso_ciclo()  #Preguntamos si quiere eliminar otro.
        elif indice_menu == 4:  #Si es 4.
            print('Mostrar Catalogo.'.center(150, ' '))
            print('Peliculas'.center(50, ' '))
            mostrar(pelicula)
            print('Series'.center(50, ' '))            #Mostramos.
            mostrar(serie)
            print('Documental'.center(50, ' '))
            mostrar(documental)
            print('Eventos Deportivos'.center(50, ' '))
            mostrar(evento_deportivo)
            time.sleep(8)
        elif indice_menu == 5:  #Si es 5.
            while a:
                print('Cargar Catalogo'.center(100, ' '))
                print('Las categorias de Catalogos son:')
                print('1.- Peliculas.')
                print('2.- Series.')                     #Mostramos un menú de las categorias.
                print('3.- Documental.')
                print('4.- Evento Deportivo.')
                while True:
                    respuesta_menu = input('Ingrese el numero de opción que desea:\n')  #Pedimos que ingrese el número de la opción deseada.
                    if respuesta_menu.isdigit() and (1 <= int(respuesta_menu) <= 4):  #Condición para que verifique que el número ingresado sea dígito y tiene que estar dentro de los valores.
                        respuesta_menu = int(respuesta_menu)
                        break
                    else:
                        print('No es valido.')  #Si no es un número no se hara valído.
                        continue
                nombre_archivo = input('Ingresa el Nombre del archivo:\n')  #Pedimos el nombre del archivo a cargar.
                if respuesta_menu == 1:  #Si es 1.
                    pelicula = leer_archivo(nombre_archivo)  #El resultado lo guardara en el arreglo "pelicula".
                elif respuesta_menu == 2:   #Si es 2.
                    serie = leer_archivo(nombre_archivo)  #El resultado lo guardara en el arreglo "serie".
                elif respuesta_menu == 3:   #Si es 3.
                    documental = leer_archivo(nombre_archivo)  #El resultado lo guardara en el arreglo "documental".
                else:
                    evento_deportivo = leer_archivo(nombre_archivo)  #El resultado lo guardara en el arreglo "evento_deportivo".
                a = regreso_ciclo()  #Preguntamos si quiere cargar otro.
        elif indice_menu == 6:   #Si es 6.
            guardar_catalogo(pelicula, 'Catalogo_de_Peliculas.txt')
            guardar_catalogo(serie, 'Catalogo_de_Series.txt')            #Se crea un archivo de texto.
            guardar_catalogo(documental, 'Catalogo_de_Documentales.txt')
            guardar_catalogo(evento_deportivo, 'Catalogo_de_Eventos_Deportivos.txt')
        else:
            respuesta = salir_prog()  #Termina el programa.

main()
