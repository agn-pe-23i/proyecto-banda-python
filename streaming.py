import time
import os  # Librerías


def regreso_ciclo():
    respuesta = input('Quiere repetir la operación? [S/otra letra]\n')  # Se pide si se quiere regresar a la operación
    if respuesta.isalpha() and respuesta.lower() == 's':  # Verificamos que sea una letra y que sea 's'
        respuesta = True  # de serlo devuelve un verdadero
    else:
        respuesta = False  # de lo contrario un falso
    return respuesta  # regresa la respuesta


def mostrar(variante):
    for i in variante:  # para cada diccionario del arreglo
        for i_2 in i:  # para cada elemento del diccionario
            print(i_2)   # Se muestra el título de diccionario
            print(i[i_2])  # Se muestra el contenido del diccionario
    return   # No hay nada que retornar al código


def opciones():
    print('Seleccione la opción deseada'.center(100, ' '))
    print('='.center(100, '='))
    print('1.- Pelicula.')
    print('2.- Serie.')
    print('3.- Documental.')            # Se muestran las opciones
    print('4.- Evento deportivo.')
    print('5.- Salir.')
    respuesta = input('Ingrese la opción deseada\n')   # Se pide que escoja una
    if respuesta.isdigit() and (1 <= int(respuesta) <= 5):  # verificamos que sea un número y este entre el 1 y 5
        respuesta = int(respuesta)   # de serlo lo hacemos entero
        b = True   # y mandamos un verdadero para continuar en el código
    else:
        print('No es valido.')    # de lo contrario indicamos que no es válido
        b = False   # y mandamos un falso para volver a hacer la operación
    return respuesta, b   # retornamos la respuesta del número y "b" si es verdadero o falso


def salir_prog():
    while True:  # Ciclo para verificar que los datos sean correctos
        respuesta = input('Seguro quieres salir?  [S/N]\n')   # Preguntamos si esta seguro de salir
        if respuesta.isalpha():   # Si la respuesta fue una letra
            if respuesta.lower() == 's':  # Y además fue una s
                respuesta = 'N'  # hacemos una N para el programa principal
                break   # cerramos el ciclo de verificación
            elif respuesta.lower() == 'n':   # de ser una N
                respuesta = 'S'   # Regresamos una S al programa principal
                break   # cerramos el ciclo de verificación
            else:   # si no fue ninguna de nuestras opciones
                print('No es un carácter valido.')  # decimos que no es un carácter valido
                continue   # y volvemos a hacer la operación
        else:  # si no fue una letra
            print('No es una letra.')   # decimos que no fue una letra
            continue   # y volvemos a hacer la operación
    return respuesta  # regresamos la respuesta al programa principal


def crear_archivo(arreg, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:  # Creamos un archivo con un nombre en especial
        for diccionario in arreg:  # para cada diccionario en el arreglo
            oration = ' '.join([f"{clave}: {valor}" for clave, valor in diccionario.items()])  # hacemos que cada
            archivo.write(oration + '\n')       # diccionario sea una línea u oración.


def guardar_catalogo(catalogo):
    b = True  # inicializamos el ciclo
    os.system('cls')  # limpiamos pantalla
    print('Guardar Catalogo'.center(100, ' '))  # colocamos un bonito encabezado
    while b:  # ciclo de comprobación
        respuesta, b = opciones()   # pedimos una especificación (pelicula, serie, etc.) y se verifica que sea válido
        if respuesta == 1:  # si fue 1
            nombre_archivo = input('Ingresa un nombre para el catálogo de películas.\n')  # pide un nombre para
            #                                                                               películas
            crear_archivo(catalogo[0], nombre_archivo)  # crea un archivo de nombre antes solicitado compuesto de 
            #                                             el primer arreglo del catálogo general
            break
        elif respuesta == 2:  # si fue 2
            nombre_archivo = input('Ingresa un nombre para el catálogo de Series.\n')  # pide un nombre para series
            crear_archivo(catalogo[1], nombre_archivo)  # crea un archivo de nombre antes solicitado compuesto de 
            #                                               el segundo arreglo del catálogo general
            break
        elif respuesta == 3:  # si fue 3
            nombre_archivo = input('Ingresa un nombre para el catalogo de Documentales.\n')  # pide un nombre
            crear_archivo(catalogo[2], nombre_archivo)  # crea un archivo de nombre antes solicitado compuesto de 
            #                                               el tercer arreglo del catálogo general
            break
        elif respuesta == 4:  # si fue 4
            nombre_archivo = input('Ingresa un nombre para el catalogo de Eventos Deportivos.\n')  # pide un nombre
            crear_archivo(catalogo[3], nombre_archivo)  # crea un archivo de nombre antes solicitado compuesto de 
            #                                             el cuarto arreglo del catálogo general

            break
        else:
            b = False  # si no fue ninguno termina el ciclo
    return  # no regresa nada al programa principal


def leer_archivo(nombre_archivo):
    try:  # Verifica que exista el archivo
        with open(nombre_archivo, 'r') as archivo:  # abre el archivo solo en lectura
            lineas = archivo.readlines()  # lee el contenido por líneas
        arreglo_diccionarios = []  # crea el arreglo donde se guardaran los datos
        for linea in lineas:  # para cada palabra en cada línea
            palabras = linea.strip().split()  # las separa
            if len(palabras) >= 2:  # con las dos primeras palabras
                clave = ' '.join(palabras[:2])  # genera el título del producto
                diccionario = {clave: ' '.join(palabras[2:])}  # el resto es la información del producto
                arreglo_diccionarios.append(diccionario)  # lo agrega al arreglo
        return arreglo_diccionarios  # regresa el arreglo con los datos
    except FileNotFoundError:  # de no existir
        arreglo_diccionarios = []  # deja el arreglo en blanco
        print("El archivo no fue encontrado.")  # indica que no fue encontrado
        return arreglo_diccionarios  # regresa el arreglo de datos


def cargar_catalogo(catalogo):
    b = True  # inicializamos el ciclo de verificación
    os.system('cls')  # limpiamos pantalla
    print('Cargar Catalogo'.center(100, ' '))  # mostramos un bonito titulo
    while b:  # ciclo de verificación
        respuesta_menu, b = opciones()  # pedimos una especificación (pelicula, serie, etc.) y se verifica 
        #                                    que sea válido
        if 1 <= respuesta_menu <= 4:  # si la respuesta está entre uno y cuatro
            nombre_archivo = input('Ingresa el Nombre del archivo:\n')  # pide el nombre del archivo a leer
            catalogo[respuesta_menu - 1] = leer_archivo(nombre_archivo)  # mandamos la información a una posición
            #                                                               especial del arreglo (1 es películas,
            #                                                               2 es series, 3 es documentales, etc.)
            break  # terminamos el ciclo
        else:  # de lo contrario
            b = False  # cerramos el ciclo
    return catalogo  # regresamos el catálogo general


def mostrar_catalogo(catalogo):
    os.system('cls')  # limpiar pantalla
    b = True  # inicializa el ciclo de verificación
    while b:  # ciclo de verificación
        print('Mostrar Catalogo'.center(100, ' '))  # mostramos un bonito titulo
        respuesta, b = opciones()  # pedimos una especificación (pelicula, serie, etc.) y se verifica que sea válido
        if respuesta == 1:  # si fue uno
            pelicula_1 = catalogo[0]  # ingresamos a una variable el primer arreglo del catalogo
            mostrar(pelicula_1)  # mostramos ese primer arreglo
            time.sleep(8)  # se queda quieta la pantalla por 8 segundos para mostrarlo
        elif respuesta == 2:  # sí fue dos
            serie_1 = catalogo[1]  # ingresamos a una variable el segundo arreglo del catálogo
            mostrar(serie_1)  # mostramos ese segundo arreglo
            time.sleep(8)  # se queda quieta la pantalla por 8 segundos para mostrarlo
        elif respuesta == 3:  # sí fue tres
            documental_1 = catalogo[2]  # ingresamos a una variable el tercer arreglo del catálogo
            mostrar(documental_1)  # mostramos ese tercer arreglo
            time.sleep(8)  # se queda quieta la pantalla por 8 segundos para mostrarlo
        elif respuesta == 4:  # sí fue cuatro
            evento_deportivo_1 = catalogo[3]  # ingresamos a una variable el cuarto arreglo del catálogo
            mostrar(evento_deportivo_1)  # mostramos ese cuarto arreglo
            time.sleep(8)  # se queda quieta la pantalla por 8 segundos para mostrarlo
        else:  # de lo contrario
            b = False  # se termina el ciclo
    return  # no regresa nada al programa principal


def eliminar_producto(catalogo_general):
    os.system('cls')  # limpiar pantalla
    print('Eliminar Producto'.center(100, ' '))  # mostramos un bonito titulo
    titulo = input('Ingresa el titulo que quieres eliminar.\n')  # pedimos el título a eliminar
    respuestas = buscar_producto(catalogo_general, titulo)  # verificamos que ese titulo exista
    if respuestas:  # si existe ese diccionario
        respuesta = input('Seguro quieres eliminarlo? [S/otra letra]\n').upper()  # verificamos que ya encontrado
        #                                                                           realmente quiera eliminarlo
        if respuesta == 'S':  # si la respuesta fue s
            for i in catalogo_general:  # buscamos dentro del primer arreglo
                for i_2 in i:  # buscamos en cada diccionario
                    if [i_2] == respuestas:  # el diccionario que sea igual al anterior buscado
                        i.remove(i_2)  # se elimina
                        print(f"Producto' {titulo} 'eliminado del catalogo.")  # mostramos una leyenda de que se elimino
                        break  # rompemos el ciclo
        else:  # de lo contrario
            return  # no hace nada
    else:  # de lo contrario
        print(f"No se encontró el producto '  {titulo}  'en el catálogo.")  # decimos que no encontramos el producto 
        #                                                                     a eliminar
    return catalogo_general  # regresamos el catalogo general al programa principal


def buscar_producto(catalogo_general, palabras_clave):
    resultados = []  # se crea un arreglo vacío donde ira el diccionario buscado
    for producto in catalogo_general:  # para cada arreglo del catálogo en general
        for i in producto:  # para cada diccionario dentro del arreglo
            if palabras_clave in i:  # buscamos coincidencias en los títulos
                resultados.append(i)  # de haberlas se agrega ese diccionario al arreglo respuesta
                break  # se termina el ciclo
            for i_2 in i:  # para cada título
                if palabras_clave in i_2:  # buscamos coincidencias en los títulos
                    resultados.append(i)  # de haberlas se agrega ese diccionario al arreglo respuesta
                    break  # se termina el ciclo
                for i_3 in i[i_2]:  # para cada contenido dentro del diccionario
                    if palabras_clave in i_3:  # buscamos coincidencias en el contenido del diccionario
                        resultados.append(i)  # de haberlas se agrega ese diccionario al arreglo respuesta
                        break  # se termina el ciclo
    if resultados:  # sí hubo resultados de la búsqueda
        print("Resultados encontrados:", '\n')  # mostramos una leyenda
        mostrar(resultados)  # y mostramos el resultado
    else:  # de lo contrario
        print("No se encontraron productos con las palabras clave proporcionadas.")  # mostramos una leyenda
    return resultados  # regresamos esos resultados


def agregar_evento():
    print('Evento deportivo1'.center(100, ' '))  # mostramos un bonito titulo
    titulo = input('Ingresa el titulo del evento deportivo.\n')  # pedimos el título
    deporte = input('Ingresa deporte del que trata.\n')  # pedimos el deporte
    fecha = input('Ingresa el periodo anual de transmisión.\n')  # pedimos el año (no me deja poner año)
    hora = input('Ingresa la hora en que se transmitió.\n')  # pedimos la hora de transmisión
    lugar = input('Ingresa el lugar de donde se llevo acabo.\n')  # pedimos el lugar
    evento = {titulo: 'Deporte: ' + deporte + ' Periodo anual de lanzamiento: ' + fecha + ' Hora de transmisión: '
                      + hora + ' Lugar: ' + lugar}  # creamos el diccionario
    return evento  # regresamos el diccionario al módulo agregar


def agregar_documental():
    print('Documental'.center(100, ' '))  # mostramos un bonito titulo
    titulo = input('Ingresa el titulo del documental\n')  # pedimos el título
    tema = input('Ingresa el tema del documental\n')  # pedimos el tema
    director = input('Ingresa el director del documental\n')  # pedimos el director
    fecha = input('Ingresa el periodo anual de lanzamiento del documental\n')  # pedimos el año (no me deja poner año)
    documental = {titulo: 'Tema: ' + tema + ' Director: ' + director + ' Periodo anual lanzamiento: ' + fecha}  #
    #                                                                                             creamos el diccionario
    return documental  # regresamos el diccionario al módulo agregar


def agregar_serie():
    print('Serie'.center(100, ' '))  # mostramos un bonito titulo
    titulo = input('Ingresa el titulo de la serie\n')  # pedimos el título
    actor = input('Ingresa el actor principal de la serie\n')  # pedimos el actor principal
    director = input('Ingresa el director de la serie\n')  # pedimos el director
    temporadas = input('Ingresa las temporadas de la serie\n')  # pedimos el número de temporadas
    serie = {titulo: 'Actor principal: ' + actor + ' Temporadas: ' + temporadas + ' Director: ' + director}  # creamos 
    #                                                                                                     el diccionario
    return serie  # regresamos el diccionario al módulo agregar


def agregar_peli():
    print('Pelicula'.center(100, ' '))  # mostramos un bonito titulo
    titulo = input('Ingresa el titulo de la pelicula.\n')  # pedimos el título
    actor = input('Ingresa el actor principal de la pelicula.\n')  # pedimos el actor principal
    fecha = input('Ingresa el periodo anual de lanzamiento de la pelicula.\n')  # pedimos el año (no me deja poner año)
    director = input('Ingresa el director de la pelicula.\n')  # pedimos el director
    peli = {titulo: 'Actor principal: ' + actor + ' Periodo anual de lanzamiento: ' + fecha + ' Director: ' + director}
    #                                                                                           creamos el diccionario
    return peli  # regresamos el diccionario al módulo agregar


def agregar_producto(catalogo_general):
    respuesta_2 = 'S'
    respuesta = 'S'
    a = True            # inicializamos ciclos
    b = True
    while respuesta_2 == 'S':  # ciclo para repetir o salir
        os.system('cls')  # limpiar pantalla
        print('Agregar Producto'.center(100, ' '))  # mostramos un bonito titulo
        while b:  # ciclo para verificar opciones
            respuesta_2, b = opciones()  # pedimos una especificación (pelicula, serie, etc.) y se verifica
            #                               que sea valido
            if respuesta_2 == 1:  # Sí fue uno
                while a:  # ciclo para repetir proceso
                    catalogo_general[0].append(agregar_peli())  # agregamos el diccionario al arreglo en la posición 0
                    a = regreso_ciclo()  # verificación para saber si repetir
                break  # se termina el ciclo
            elif respuesta_2 == 2:  # sí fue dos
                while a:  # ciclo para repetir proceso
                    catalogo_general[1].append(agregar_serie())  # agregamos el diccionario al arreglo en la posición 1
                    a = regreso_ciclo()  # verificación para saber si repetir
                break  # se termina el ciclo
            elif respuesta_2 == 3:  # sí fue tres
                while a:  # ciclo para repetir proceso
                    catalogo_general[2].append(agregar_documental())  # agregamos el diccionario al arreglo en
                    #                                                   la posición 2
                    a = regreso_ciclo()  # verificación para saber si repetir
                break  # se termina el ciclo
            elif respuesta_2 == 4:  # sí fue cuatro
                while a:  # ciclo para repetir proceso
                    catalogo_general[3].append(agregar_evento())  # agregamos el diccionario al arreglo en pa posición 3
                    a = regreso_ciclo()  # verificación para saber si repetir
                break  # se termina el ciclo
            elif respuesta_2 == 5:  # sí fue cinco
                respuesta = 'S'  # colocamos "s" en respuesta para mantener el programa principal
                respuesta_2 = 'N'  # colocamos "n" para cerrar este modulo
                break  # se termina el ciclo
    return catalogo_general, respuesta  # regresamos el catálogo al programa principal junto a la respuesta


def menu():
    print('Menu Principal'.center(100, ' '))  # mostramos un bonito titulo
    print('Seleccione la opción deseada'.center(100, ' '))
    print('='.center(100, '='))
    print('1.- Agregar Producto.')
    print('2.- Buscar Producto.')
    print('3.- Eliminar Producto.')   # mostramos las opciones del programa principal
    print('4.- Mostrar Catalogo.')
    print('5.- Cargar Catalogo.')
    print('6.- Guardar Catalogo.')
    print('7.- Salir.')
    while True:  # ciclo de verificación
        respuesta_menu = input('Ingrese el numero de opción que desea:\n')  # pedimos ingrese una opción
        if respuesta_menu.isdigit() and (1 <= int(respuesta_menu) <= 7):  # si la respuesta fue un número y este entre
            #                                                               uno y siete
            respuesta_menu = int(respuesta_menu)  # convierte la respuesta en un entero
            break  # se termina el ciclo
        else:  # de lo contrario
            print('No es valido.')  # mostramos una leyenda
            continue  # repetimos el proceso
    return respuesta_menu  # regresamos la respuesta numerica al main


def inicializar():
    respuesta = 'S'
    pelicula = []
    serie = []          # inicializamos variables
    documental = []
    evento_deportivo = []
    catalogo_general = [pelicula, serie, documental, evento_deportivo]
    return respuesta, catalogo_general  # regresa la respuesta y el catálogo general


def main():
    respuesta, catalogo_general = inicializar()  # inicializamos las variables
    while respuesta == 'S':  # ciclo de proceso
        a = True
        a_1 = True
        a_2 = True   # inicializamos variables de proceso
        a_3 = True
        a_4 = True
        os.system('cls')  # limpiar pantalla
        indice_menu = menu()  # mostramos las opciones del menu y tomamos la elección
        if indice_menu == 1:  # si fue uno
            while a:  # ciclo para repetir proceso
                catalogo_general, respuesta = agregar_producto(catalogo_general)  # agregamos un producto, mandamos
                #                                                                   y recibimos el catálogo general
                a = regreso_ciclo()  # verificación para saber si repetir
        elif indice_menu == 2:  # sí fue dos
            while a_1:  # ciclo para repetir proceso
                os.system('cls')  # limpiar pantalla
                print('Buscar Producto'.center(100, ' '))  # mostramos un bonito titulo
                palabras_clave = input("Ingrese palabras clave para buscar un producto: \n")  # pedimos palabras clave
                buscar_producto(catalogo_general, palabras_clave)  # buscamos el producto
                a_1 = regreso_ciclo()  # verificación para saber si repetir
        elif indice_menu == 3:  # sí fue tres
            while a_2:  # ciclo para repetir proceso
                catalogo_general = eliminar_producto(catalogo_general)  # eliminamos un producto mandando y
                #                                                         recibiendo el catálogo general
                a_2 = regreso_ciclo()  # verificación para saber si repetir
        elif indice_menu == 4:  # sí fue cuatro
            mostrar_catalogo(catalogo_general)  # mostramos catálogo en especial
        elif indice_menu == 5:  # # si fue cinco
            while a_3:  # ciclo para repetir proceso
                catalogo_general = cargar_catalogo(catalogo_general)  # cargamos catálogo mandando y recibiendo
                #                                                       el catálogo general
                a_3 = regreso_ciclo()  # verificación para saber si repetir
        elif indice_menu == 6:  # Sí fue seis
            while a_4:  # ciclo para repetir proceso
                guardar_catalogo(catalogo_general)  # guardamos catálogo en especial en un archivo
                a_4 = regreso_ciclo()  # verificación para saber si repetir
        else:  # de lo contrario
            respuesta = salir_prog()  # verificamos si quiere salir del programa principal


main()  # llamamos al main
