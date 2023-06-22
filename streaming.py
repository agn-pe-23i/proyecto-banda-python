import time
import os  # Librerias


def regreso_ciclo():
    respuesta = input('Quiere repetir la operacion? [S/otra letra]\n')  # Se pide si se quiere regresar a la operacion
    if respuesta.isalpha() and respuesta.lower() == 's':  # Verificamos que sea una letra y que sea 's'
        respuesta = True  # de serlo eevuelve un verdadero
    else:
        respuesta = False  # de lo contrario un falso
    return respuesta  # regresa la respuesta


def mostrar(variante): 
    for i in variante:  # para cada diccionario del arreglo
        for i_2 in i:  # para cada elemento del diccionario
            print(i_2)   # Se muetra el titulo de diccionario
            print(i[i_2])  # Se muestra el contenido del diccionario
    return   # No hay nada que retornar al codigo


def opciones():
    print('Seleccione la opcion deseada'.center(100, ' '))   
    print('='.center(100, '='))
    print('1.- Pelicula.')
    print('2.- Serie.')
    print('3.- Documental.')            # Se muestran las opciones
    print('4.- Evento deportivo.')
    print('5.- Salir.')
    respuesta = input('Ingrese la opcion deseada\n')   # Se pide que escoja una
    if respuesta.isdigit() and (1 <= int(respuesta) <= 5):  # verificamos que sea un numero y este entre el 1 y 5
        respuesta = int(respuesta)   # de serlo lo hacemos entero
        b = True   # y mandamos un verdadero para continuar en el codigo
    else:
        print('No es valido.')    # de lo contrario indicamos que no es valido
        b = False   # y mandamos un falso para volver a hacer la operacion
    return respuesta, b   # retornamos la respuesta del numero y b si es verdadero o falso


def salir_prog():
    while True:  # Ciclo para verificar que los datos sean correctos
        respuesta = input('Seguro quieres salir?  [S/N]\n')   # Preguntamos si esta seguro de salir
        if respuesta.isalpha():   # Si la respuesta fue una letra
            if respuesta.lower() == 's':  # Y ademas fue una s
                respuesta = 'N'  # hacemos una N para el programa principal
                break   # cerramos el ciclo de verificacion
            elif respuesta.lower() == 'n':   # de ser una N
                respuesta = 'S'   # Regresamos una S al programa principal
                break   # cerramos el ciclo de verificacion
            else:   # si no fue ninguna de nuestras opciones
                print('No es un caracter valido.')  # decimos que no es un caracter valido
                continue   # y volvemos a hacer la operacion
        else:  # si no fue una letra
            print('No es una letra.')   # decimos que no fue una letra
            continue   # y volvemos a hacer la operacion
    return respuesta  # regresamos la respuesta al programa principal


def crear_archivo(arreg, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:  # Creamos un archivo con un nombre en especial
        for diccionario in arreg:  # para cada diccionario en el arreglo
            oracion = ' '.join([f"{clave}: {valor}" for clave, valor in diccionario.items()])  # hacemos que cada 
            archivo.write(oracion + '\n')       # diccionario sea una linea u oracion.


def guardar_catalogo(catalogo):
    b = True  # inicializamos el ciclo
    os.system('cls')  # limpiamos pantalla
    print('Guardar Catalogo'.center(100, ' '))  # colocamos un bonito encabezado
    while b:  # ciclo de comprobacion
        respuesta, b = opciones()   # pedimos una especificaion (pelicula, serie, etc.) y se verifica que sea valido 
        if respuesta == 1:  # si fue 1
            nombre_archivo = input('Ingresa un nombre para el catalogo de Peliculas.\n')  # pide un nombre para 
            #                                                                               peliculas
            crear_archivo(catalogo[0], nombre_archivo)  # crea un archivo de nombre antes solicitado compuesto de el 
            #                                             primer arreglo del catalogo general
            break
        elif respuesta == 2:  # si fue 2
            nombre_archivo = input('Ingresa un nombre para el catalogo de Series.\n')  # pide un nombre para series
            crear_archivo(catalogo[1], nombre_archivo)  # crea un archivo de nombre antes solicitado compuesto de el 
            #                                             segundo arreglo del catalogo general
            break
        elif respuesta == 3:  # si fue 3 
            nombre_archivo = input('Ingresa un nombre para el catalogo de Documentales.\n')  # pide un nombre
            crear_archivo(catalogo[2], nombre_archivo)  # crea un archivo de nombre antes solicitado compuesto de el 
            #                                             tercer arreglo del catalogo general
            break
        elif respuesta == 4:  # si fue 4
            nombre_archivo = input('Ingresa un nombre para el catalogo de Eventos Deportivos.\n')  # pide un nombre
            crear_archivo(catalogo[3], nombre_archivo)  # crea un archivo de nombre antes solicitado compuesto de el 
            #                                             cuarto arreglo del catalogo general

            break
        else:
            b = False  # si no fue ninguno termina el ciclo
    return  # no regresa nada al programa principal


def leer_archivo(nombre_archivo):
    try:  # Verifica que exista el archivo
        with open(nombre_archivo, 'r') as archivo:  # abre el archivo solo en lectura
            lineas = archivo.readlines()  # lee el contenido por lineas
        arreglo_diccionarios = []  # crea el arreglo donde se guardaran los datos
        for linea in lineas:  # para cada palabra en cada linea
            palabras = linea.strip().split()  # las separa
            if len(palabras) >= 2:  # con las dos primeras palabras
                clave = ' '.join(palabras[:2])  # genera el titulo del producto
                diccionario = {clave: ' '.join(palabras[2:])}  # el resto es la informacion del producto
                arreglo_diccionarios.append(diccionario)  # lo agrega al arreglo
        return arreglo_diccionarios  # regresa el arreglo con los datos
    except FileNotFoundError:  # de no existir
        arreglo_diccionarios = []  # deja el arreglo en blanco
        print("El archivo no fue encontrado.")  # indica que no fue encontrado
        return arreglo_diccionarios  # regresa el arreglo de datos


def cargar_catalogo(catalogo):
    b = True  # inicializamos el ciclo de verificaion 
    os.system('cls')  # impiamos pantalla
    print('Cargar Catalogo'.center(100, ' '))  # mostramos un bonito titulo
    while b:  # ciclo de verificacion
        respuesta_menu, b = opciones()  # pedimos una especificaion (pelicula, serie, etc.) y se verifica que sea valido
        if 1 <= respuesta_menu <= 4:  # si la respuesta esta entre uno y cuatro
            nombre_archivo = input('Ingresa el Nombre del archivo:\n')  # pide el nombre del archivo a leer
            catalogo[respuesta_menu - 1] = leer_archivo(nombre_archivo)  # mandamos la informacion a una pocision 
            #                                                               especial del arreglo (1 es peliculas, 
            #                                                               2 es series, 3 es documentales, etc.)
            break  # terminamos el ciclo
        else:  # de lo contrario
            b = False  # cerramos el ciclo
    return catalogo  # regresamos el catalogo general


def mostrar_catalogo(catalogo):
    os.system('cls')
    b = True
    while b:
        print('Mostrar Catalogo'.center(100, ' '))
        respuesta, b = opciones()
        if respuesta == 1:
            pelicula_1 = catalogo[0]
            mostrar(pelicula_1)
            time.sleep(8)
        elif respuesta == 2:
            serie_1 = catalogo[1]
            mostrar(serie_1)
            time.sleep(8)
        elif respuesta == 3:
            documental_1 = catalogo[2]
            mostrar(documental_1)
            time.sleep(8)
        elif respuesta == 4:
            evento_deportivo_1 = catalogo[3]
            mostrar(evento_deportivo_1)
            time.sleep(8)
        else:
            b = False
    return


def eliminar_producto(catalogo_general):
    os.system('cls')
    print('Eliminar Producto'.center(100, ' '))
    titulo = input('Ingresa el titulo que quieres eliminar.\n')
    respuestas = buscar_producto(catalogo_general, titulo)
    respuesta = input('Seguro quieres eliminarlo? [S/otra letra]\n').upper()
    if respuestas:
        if respuesta == 'S':
            for i in catalogo_general:
                for i_2 in i:
                    if [i_2] == respuestas:
                        i.remove(i_2)
                        print(f"Producto' {titulo} 'eliminado del catalogo.")
                        break
        else:
            return
    else:
        print(f"No se encontro el producto '  {titulo}  'en el catalogo.")
    return catalogo_general


def buscar_producto(catalogo_general, palabras_clave):
    resultados = []
    for producto in catalogo_general:
        for i in producto:
            if palabras_clave in i:
                resultados.append(i)
                break
            for i_2 in i:
                if palabras_clave in i_2:
                    resultados.append(i)
                    break
                for i_3 in i[i_2]:
                    if palabras_clave in i_3:
                        resultados.append(i)
                        break
    if resultados:
        print("Resultados encontrados:", '\n')
        mostrar(resultados)
    else:
        print("No se encontraron productos con las palabras clave proporcionadas.")
    return resultados


def agregar_evento():
    print('Evento deportivo1'.center(100, ' '))
    titulo = input('Ingresa el titulo del evento deportivo.\n')
    deporte = input('Ingresa deporte del que trata.\n')
    fecha = input('Ingresa el periodo anual de transmicion.\n')
    hora = input('Ingresa la hora en que se transimitio.\n')
    lugar = input('Ingresa el lugar de donde se llevo acabo.\n')
    evento = {titulo: 'Deporte: ' + deporte + ' Periodo anual de lanzamiento: ' + fecha + ' Hora de transmicion: '
                      + hora + ' Lugar: ' + lugar}
    return evento


def agregar_documental():
    print('Documental'.center(100, ' '))
    titulo = input('Ingresa el titulo del documental\n')
    tema = input('Ingresa el tema del documental\n')
    director = input('Ingresa el director del documental\n')
    fecha = input('Ingresa el periodo anual de lanzamiento del documental\n')
    documental = {titulo: 'Tema: ' + tema + ' Director: ' + director + ' Periodo anual lanzamiento: ' + fecha}
    return documental


def agregar_serie():
    print('Serie'.center(100, ' '))
    titulo = input('Ingresa el titulo de la serie\n')
    actor = input('Ingresa el actor principal de la serie\n')
    director = input('Ingresa el director de la serie\n')
    temporadas = input('Ingresa las temporadas de la serie\n')
    serie = {titulo: 'Actor pricipal: ' + actor + ' Temporadas: ' + temporadas + ' Director: ' + director}
    return serie


def agregar_peli():
    print('Pelicula'.center(100, ' '))
    titulo = input('Ingresa el titulo de la pelicula.\n')
    actor = input('Ingresa el actor principal de la pelicula.\n')
    fecha = input('Ingresa el periodo anual de lanzamiento de la pelicula.\n')
    director = input('Ingresa el director de la pelicula.\n')
    peli = {titulo: 'Actor principal: ' + actor + ' Periodo anual de lanzamiento: ' + fecha + ' Director: ' + director}
    return peli


def agregar_producto(catalogo_general):
    respuesta_2 = 'S'
    respuesta = 'S'
    a = True
    b = True
    while respuesta_2 == 'S':
        os.system('cls')
        print('Agregar Producto'.center(100, ' '))
        while b:
            respuesta_2, b = opciones()
            if respuesta_2 == 1:
                while a:
                    catalogo_general[0].append(agregar_peli())
                    a = regreso_ciclo()
                break
            elif respuesta_2 == 2:
                while a:
                    catalogo_general[1].append(agregar_serie())
                    a = regreso_ciclo()
                break
            elif respuesta_2 == 3:
                while a:
                    catalogo_general[2].append(agregar_documental())
                    a = regreso_ciclo()
                break
            elif respuesta_2 == 4:
                while a:
                    catalogo_general[3].append(agregar_evento())
                    a = regreso_ciclo()
                break
            elif respuesta_2 == 5:
                respuesta = 'S'
                respuesta_2 = 'N'
                break
    return catalogo_general, respuesta


def menu():
    print('Menu Principal'.center(100, ' '))
    print('Seleccione la opcion deseada'.center(100, ' '))
    print('='.center(100, '='))
    print('1.- Agregar Producto.')
    print('2.- Buscar Producto.')
    print('3.- Eliminar Producto.')
    print('4.- Mostrar Catalogo.')
    print('5.- Cargar Catalogo.')
    print('6.- Guardar Catalogo.')
    print('7.- Salir.')
    while True:
        respuesta_menu = input('Ingrese el numero de opcion que desea:\n')
        if respuesta_menu.isdigit() and (1 <= int(respuesta_menu) <= 7):
            respuesta_menu = int(respuesta_menu)
            break
        else:
            print('No es valido.')
            continue
    return respuesta_menu


def inicializar():
    respuesta = 'S'
    pelicula = []
    serie = []
    documental = []
    evento_deportivo = []
    catalogo_general = [pelicula, serie, documental, evento_deportivo]
    return respuesta, catalogo_general


def main():
    respuesta, catalogo_general = inicializar()
    while respuesta == 'S':
        a = True
        a_1 = True
        a_2 = True
        a_3 = True
        a_4 = True
        os.system('cls')
        indice_menu = menu()
        if indice_menu == 1:
            while a:
                catalogo_general, respuesta = agregar_producto(catalogo_general)
                a = regreso_ciclo()
        elif indice_menu == 2:
            while a_1:
                os.system('cls')
                print('Buscar Producto'.center(100, ' '))
                palabras_clave = input("Ingrese palabras clave para buscar un producto: \n")
                buscar_producto(catalogo_general, palabras_clave)
                a_1 = regreso_ciclo()
        elif indice_menu == 3:
            while a_2:
                catalogo_general = eliminar_producto(catalogo_general)
                a_2 = regreso_ciclo()
        elif indice_menu == 4:
            mostrar_catalogo(catalogo_general)
        elif indice_menu == 5:
            while a_3:
                catalogo_general = cargar_catalogo(catalogo_general)
                a_3 = regreso_ciclo()
        elif indice_menu == 6:
            while a_4:
                guardar_catalogo(catalogo_general)
                a_4 = regreso_ciclo()
        else:
            respuesta = salir_prog()


main()
