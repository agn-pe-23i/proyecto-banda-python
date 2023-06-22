import time
import os  # Librerías.


def regreso_ciclo():
    respuesta = input('Quiere repetir la operacion? [S/otra letra]\n')  #Se pide si se quiere regresar a la operación.
    if respuesta.isalpha() and respuesta.lower() == 's':  #Verificamos que sea una letra y que sea 's'.
        respuesta = True  #De serlo devuelve un verdadero.
    else:
        respuesta = False  #De lo contrario un falso.
    return respuesta  #Regresa la respuesta.


def mostrar(variante): 
    for i in variante:  #Para cada diccionario del arreglo.
        for i_2 in i:  #Para cada elemento del diccionario.
            print(i_2)   #Se muestra el título del diccionario.
            print(i[i_2])  #Se muestra el contenido del diccionario.
    return   #No hay nada que retornar al codigo.


def opciones():
    print('Seleccione la opcion deseada'.center(100, ' '))  #Colocamos un bonito encabezado.
    print('='.center(100, '='))
    print('1.- Pelicula.')
    print('2.- Serie.')
    print('3.- Documental.')            #Se muestran las opciones.
    print('4.- Evento deportivo.')
    print('5.- Salir.')
    respuesta = input('Ingrese la opcion deseada\n')   #Se pide que escoja una opción.
    if respuesta.isdigit() and (1 <= int(respuesta) <= 5):  #Verificamos que sea un número y este entre el 1 y 5.
        respuesta = int(respuesta)   #De serlo se convierte a entero.
        b = True   #Y mandamos un verdadero para continuar en el codigo.
    else:
        print('No es valido.')    #De lo contrario indicamos que no es válido.
        b = False   #Y mandamos un falso para volver a hacer la operación.
    return respuesta, b   #Retornamos la respuesta del número y "b" si es verdadero o falso.


def salir_prog():
    while True:  #Ciclo para verificar que los datos sean correctos.
        respuesta = input('Seguro quieres salir?  [S/N]\n')   #Preguntamos si esta seguro de salir.
        if respuesta.isalpha():   #Si la respuesta fue una letra.
            if respuesta.lower() == 's':  #Y ademas fue una "s".
                respuesta = 'N'  #Hacemos una "N" para el programa principal.
                break   #Cerramos el ciclo de verificación.
            elif respuesta.lower() == 'n':   #De ser una "N".
                respuesta = 'S'   #Regresamos una "S" al programa principal.
                break   #Cerramos el ciclo de verificación.
            else:   #Si no fue ninguna de nuestras opciones.
                print('No es un caracter valido.')  #Decimos que "no es un caracter válido".
                continue   #Y volvemos a hacer la operación.
        else:  #Si no fue una letra.
            print('No es una letra.')  #Decimos que "no fue una letra".
            continue   #Y volvemos a hacer la operación.
    return respuesta  #Regresamos la respuesta al programa principal.


def crear_archivo(arreg, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:  #Creamos un archivo con un nombre en especial.
        for diccionario in arreg:  #Para cada diccionario en el arreglo.
            oracion = ' '.join([f"{clave}: {valor}" for clave, valor in diccionario.items()])  #Hacemos que cada 
            archivo.write(oracion + '\n')                                                      #diccionario sea una línea
                                                                                               #u oración.

def guardar_catalogo(catalogo):
    b = True  #Inicializamos el ciclo.
    os.system('cls')  #Limpiamos pantalla.
    print('Guardar Catalogo'.center(100, ' '))  #Mostramos un bonito título.
    while b:  #Ciclo de comprobación.
        respuesta, b = opciones()   #Pedimos una especificación (película, serie, etc.) y se verifica que sea válido. 
        if respuesta == 1:  #Si fue 1.
            nombre_archivo = input('Ingresa un nombre para el catalogo de Peliculas.\n')  #Pide un nombre para 
                                                                                          #películas.
            crear_archivo(catalogo[0], nombre_archivo)  #Crea un archivo de nombre antes solicitado compuesto de el 
                                                        #primer arreglo del catálogo general.
            break
        elif respuesta == 2:  #Si fue 2.
            nombre_archivo = input('Ingresa un nombre para el catalogo de Series.\n')  #Pide un nombre para series.
            crear_archivo(catalogo[1], nombre_archivo)  #Crea un archivo de nombre antes solicitado compuesto de el 
                                                        #segundo arreglo del catálogo general.
            break
        elif respuesta == 3:  #Si fue 3. 
            nombre_archivo = input('Ingresa un nombre para el catalogo de Documentales.\n')  #Pide un nombre.
            crear_archivo(catalogo[2], nombre_archivo)  #Crea un archivo de nombre antes solicitado compuesto de el 
                                                        #tercer arreglo del catálogo general.
            break
        elif respuesta == 4:  # si fue 4
            nombre_archivo = input('Ingresa un nombre para el catalogo de Eventos Deportivos.\n')  #Pide un nombre.
            crear_archivo(catalogo[3], nombre_archivo)  #Crea un archivo de nombre antes solicitado compuesto de el 
                                                        #cuarto arreglo del catálogo general.

            break
        else:
            b = False  #Si no fue ninguno termina el ciclo.
    return  #No regresa nada al programa principal.


def leer_archivo(nombre_archivo):
    try:  #Verifica que exista el archivo.
        with open(nombre_archivo, 'r') as archivo:  #Abre el archivo solo en lectura.
            lineas = archivo.readlines()  #Lee el contenido por líneas.
        arreglo_diccionarios = []  #Crea el arreglo en el cual se guardarán los datos.
        for linea in lineas:  #Para cada palabra en cada línea.
            palabras = linea.strip().split()  #Las separa.
            if len(palabras) >= 2:  #Con las dos primeras palabras.
                clave = ' '.join(palabras[:2])  #Genera el título del producto.
                diccionario = {clave: ' '.join(palabras[2:])}  #El resto es la información del producto.
                arreglo_diccionarios.append(diccionario)  #Lo agrega al arreglo.
        return arreglo_diccionarios  #Regresa el arreglo con los datos.
    except FileNotFoundError:  #De no existir.
        arreglo_diccionarios = []  #Deja el arreglo en blanco.
        print("El archivo no fue encontrado.")  #Indica que no fue encontrado.
        return arreglo_diccionarios  #Regresa el arreglo de datos.


def cargar_catalogo(catalogo):
    b = True  #Inicializamos el ciclo de verificación. 
    os.system('cls')  #Limpiamos pantalla.
    print('Cargar Catalogo'.center(100, ' '))  #Mostramos un bonito título.
    while b:  #Ciclo de verificación.
        respuesta_menu, b = opciones()  #Pedimos una especificaión (película, serie, etc.) y se verifica que sea válido.
        if 1 <= respuesta_menu <= 4:  #Si la respuesta esta entre uno y cuatro.
            nombre_archivo = input('Ingresa el Nombre del archivo:\n')  #Pide el nombre del archivo a leer.
            catalogo[respuesta_menu - 1] = leer_archivo(nombre_archivo)  #Mandamos la información a una pocisión 
                                                                         #especial del arreglo (1 es pelpiculas, 
                                                                         #2 es series, 3 es documentales, etc.)
            break  #Terminamos el ciclo.
        else:  #De lo contrario.
            b = False  #Cerramos el ciclo.
    return catalogo  #Regresamos el catálogo general.


def mostrar_catalogo(catalogo):
    os.system('cls')
    b = True
    while b:
        print('Mostrar Catalogo'.center(100, ' '))  #Mostramos un bonito título.
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
    print('Eliminar Producto'.center(100, ' '))  #Mostramos un bonito título.
    titulo = input('Ingresa el título que quieres eliminar.\n')  #Colocamos un bonito encabezado.
    respuestas = buscar_producto(catalogo_general, titulo)   #Busca el porducto específico y lo agrega a "respuesta".
    respuesta = input('Seguro quieres eliminarlo? [S/otra letra]\n').upper()  #Preguntamos si está seguro de eliminar el producto.
    if respuestas:
        if respuesta == 'S':
            for i in catalogo_general:
                for i_2 in i:
                    if [i_2] == respuestas:
                        i.remove(i_2)
                        print(f"Producto' {titulo} 'eliminado del catálogo.")  #Mostramos en pantalla que el producto fue eliminado.
                        break
        else:
            return
    else:
        print(f"No se encontro el producto '  {titulo}  'en el catálogo.")  #Si el título que desea elimnar no se encuentra, dira que no fue encontrado.
    return catalogo_general


def buscar_producto(catalogo_general, palabras_clave):
    resultados = []  #Lista para guardar los resultados encontrados.
    for producto in catalogo_general:  #Ciclo para buscar el "producto" en la lista catalogo_general.
        for i in producto:
            if palabras_clave in i:  #Si se encuentra dentro del contenido.
                resultados.append(i)  #Se agregara a la lista.
                break
            for i_2 in i:
                if palabras_clave in i_2:   #Si se encuentra dentro del contenido.
                    resultados.append(i)  #Se agregara a la lista.
                    break
                for i_3 in i[i_2]:
                    if palabras_clave in i_3:   #Si se encuentra dentro del contenido.
                        resultados.append(i)  #Se agregara a la lista.
                        break
    if resultados:
        print("Resultados encontrados:", '\n')  #Muestra en pantalla los resultados encontrados.
        mostrar(resultados)
    else:
        print("No se encontraron productos con las palabras clave proporcionadas.")  #Decimos que no sse encontraron productos.
    return resultados  #Devuelve resultados.


def agregar_evento():
    print('Evento deportivo1'.center(100, ' '))  #Mostramos un bonito título.
    titulo = input('Ingresa el título del evento deportivo.\n')
    deporte = input('Ingresa deporte del que trata.\n')
    fecha = input('Ingresa el periodo anual de transmisión.\n')    #Pedimos que ingrese los datos solicitados del evento deportivo.
    hora = input('Ingresa la hora de transmisión.\n')
    lugar = input('Ingresa el lugar de donde se lleva acabo.\n')
    evento = {titulo: 'Deporte: ' + deporte + ' Periodo anual de lanzamiento: ' + fecha + ' Hora de transmisión: '
                      + hora + ' Lugar: ' + lugar}  #Variable que contiene el diccionario que se agrega al arreglo.
    return evento  #Devuelve evento.


def agregar_documental():
    print('Documental'.center(100, ' '))  #Mostramos un bonito título.
    titulo = input('Ingresa el título del documental.\n')
    tema = input('Ingresa el tema del documental.\n')      #Pedimos que ingrese los datos solicitados del evento deportivo.
    director = input('Ingresa el director del documental.\n')
    fecha = input('Ingresa el periodo anual de lanzamiento del documental.\n')
    documental = {titulo: 'Tema: ' + tema + ' Director: ' + director + ' Periodo anual lanzamiento: ' + fecha}  #Variable que contiene el diccionario que se agrega al arreglo.
    return documental  #Devuelve documental.


def agregar_serie():
    print('Serie'.center(100, ' '))  #Mostramos un bonito título.
    titulo = input('Ingresa el título de la serie.\n')
    actor = input('Ingresa el actor principal de la serie.\n')   #Pedimos que ingrese los datos solicitados del evento deportivo.
    director = input('Ingresa el director de la serie.\n')
    temporadas = input('Ingresa las temporadas de la serie.\n')
    serie = {titulo: 'Actor pricipal: ' + actor + ' Temporadas: ' + temporadas + ' Director: ' + director}  #Variable que contiene el diccionario que se agrega al arreglo.
    return serie  #Devuelve serie.


def agregar_peli():
    print('Película'.center(100, ' '))  #Mostramos un bonito título.
    titulo = input('Ingresa el título de la película.\n')
    actor = input('Ingresa el actor principal de la película.\n')   #Pedimos que ingrese los datos solicitados del evento deportivo.
    fecha = input('Ingresa el periodo anual de lanzamiento de la película.\n')
    director = input('Ingresa el director de la película.\n')
    peli = {titulo: 'Actor principal: ' + actor + ' Periodo anual de lanzamiento: ' + fecha + ' Director: ' + director}  #Variable que contiene el diccionario que se agrega al arreglo.
    return peli  #Devuelve peli.


def agregar_producto(catalogo_general):
    respuesta_2 = 'S'
    respuesta = 'S'
    a = True
    b = True
    while respuesta_2 == 'S':
        os.system('cls')
        print('Agregar Producto'.center(100, ' '))  #Mostramos un bonito título.
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
    print('Menu Principal'.center(100, ' '))  #Mostramos un bonito título.
    print('Seleccione la opcion deseada'.center(100, ' '))  #Colocamos un bonito encabezado.
    print('='.center(100, '='))
    print('1.- Agregar Producto.')
    print('2.- Buscar Producto.')
    print('3.- Eliminar Producto.')    #Mostramos todas las opciones del menú en pantalla.
    print('4.- Mostrar Catalogo.')
    print('5.- Cargar Catalogo.')
    print('6.- Guardar Catalogo.')
    print('7.- Salir.')
    while True:
        respuesta_menu = input('Ingrese el numero de opcion que desea:\n')  #Pedimos que ingrese el número de la opción deseada.
        if respuesta_menu.isdigit() and (1 <= int(respuesta_menu) <= 7):  #Verifica que el número ingresado sea dígito y tiene que estar entre 1 y 7.
            respuesta_menu = int(respuesta_menu)  #Lo convierte a entero y lo guarda.
            break
        else:  #Si no es número
            print('No es válido.')  #Decimos que "no es válido".
            continue
    return respuesta_menu  #Devuelve respuesta_menu.


def inicializar():
    respuesta = 'S'  #Inicializa para que se ejecute al menos una vez.
    pelicula = []  #Lista para las películas.
    serie = []  #Lista para las series.
    documental = []  #Lista para los docuemntales.
    evento_deportivo = []  #Lista para los eventos deportivos.
    catalogo_general = [pelicula, serie, documental, evento_deportivo]  #Lista que contiene las listas anteriores.
    return respuesta, catalogo_general  #Devuelve respuesta y catalogo_general.


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
                print('Buscar Producto'.center(100, ' '))  #Mostramos un bonito título.
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
