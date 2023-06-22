import time
import os  # Librerías


def regreso_ciclo():
    respuesta = input('Quiere repetir la operación? [S/otra letra]\n')  #Se pide si se quiere regresar a la operación.
    if respuesta.isalpha() and respuesta.lower() == 's':  # Verificamos que sea una letra y que sea 's'.
        respuesta = True  #De serlo devuelve un verdadero.
    else:
        respuesta = False  #De lo contrario un falso.
    return respuesta  #Regresa la respuesta.


def mostrar(variante):
    for i in variante:  #Para cada diccionario del arreglo.
        for i_2 in i:  #Para cada elemento del diccionario.
            print(i_2)   #Se muestra el título de diccionario.
            print(i[i_2])  #Se muestra el contenido del diccionario.
    return   #No hay nada que retornar al código.


def opciones():
    print('Seleccione la opción deseada'.center(100, ' '))
    print('='.center(100, '='))
    print('1.- Pelicula.')
    print('2.- Serie.')
    print('3.- Documental.')            #Se muestran las opciones.
    print('4.- Evento deportivo.')
    print('5.- Salir.')
    respuesta = input('Ingrese la opción deseada\n')   #Se pide que escoja una.
    if respuesta.isdigit() and (1 <= int(respuesta) <= 5):  #Verificamos que sea un número y este entre el 1 y 5.
        respuesta = int(respuesta)   #De serlo lo hacemos entero.
        b = True   #Y mandamos un verdadero para continuar en el código.
    else:
        print('No es valido.')    #De lo contrario indicamos que no es válido.
        b = False   #Y mandamos un falso para volver a hacer la operación.
    return respuesta, b   #Retornamos la respuesta del número y "b" si es verdadero o falso.


def salir_prog():
    while True:  #Ciclo para verificar que los datos sean correctos.
        respuesta = input('Seguro quieres salir?  [S/N]\n')   #Preguntamos si esta seguro de salir.
        if respuesta.isalpha():   #Si la respuesta fue una letra.
            if respuesta.lower() == 's':  #Y además fue una "s".
                respuesta = 'N'  #Hacemos una "N" para el programa principal.
                break   #Cerramos el ciclo de verificación.
            elif respuesta.lower() == 'n':   #De ser una "N".
                respuesta = 'S'   #Regresamos una "S" al programa principal.
                break   #Cerramos el ciclo de verificación.
            else:   #Si no fue ninguna de nuestras opciones.
                print('No es un carácter valido.')  #Decimos que no es un carácter válido.
                continue   #Y volvemos a hacer la operación.
        else:  #Si no fue una letra.
            print('No es una letra.')   #Decimos que no fue una letra.
            continue   #Y volvemos a hacer la operación.
    return respuesta  #Regresamos la respuesta al programa principal.


def crear_archivo(arreg, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:  #Creamos un archivo con un nombre en especial.
        for diccionario in arreg:  #Para cada diccionario en el arreglo.
            oration = ' '.join([f"{clave}: {valor}" for clave, valor in diccionario.items()])  #Hacemos que cada
            archivo.write(oration + '\n')                                                      # diccionario sea una línea
                                                                                               #u oración.

def guardar_catalogo(catalogo):
    b = True  #Inicializamos el ciclo.
    os.system('cls')  #Limpiamos pantalla.
    print('Guardar Catalogo'.center(100, ' '))  #Colocamos un bonito encabezado.
    while b:  #Ciclo de comprobación.
        respuesta, b = opciones()   #Pedimos una especificación (pelicula, serie, etc.) y se verifica que sea válido.
        if respuesta == 1:  #Si fue 1.
            nombre_archivo = input('Ingresa un nombre para el catálogo de películas.\n')  #Pide un nombre para películas.                        
            crear_archivo(catalogo[0], nombre_archivo)  #Crea un archivo de nombre antes solicitado compuesto de 
                                                        #el primer arreglo del catálogo general.
            break
        elif respuesta == 2:  #Si fue 2.
            nombre_archivo = input('Ingresa un nombre para el catálogo de Series.\n')  #Pide un nombre para series.
            crear_archivo(catalogo[1], nombre_archivo)  #Crea un archivo de nombre antes solicitado compuesto de 
                                                        #el segundo arreglo del catálogo general.
            break
        elif respuesta == 3:  #Si fue 3.
            nombre_archivo = input('Ingresa un nombre para el catalogo de Documentales.\n')  #Pide un nombre para documentales.
            crear_archivo(catalogo[2], nombre_archivo)  #Crea un archivo de nombre antes solicitado compuesto de 
                                                        #el tercer arreglo del catálogo general.
            break
        elif respuesta == 4:  #Si fue 4.
            nombre_archivo = input('Ingresa un nombre para el catalogo de Eventos Deportivos.\n')  #Pide un nombre para eventos deportivos.
            crear_archivo(catalogo[3], nombre_archivo)  #Crea un archivo de nombre antes solicitado compuesto de 
                                                        #el cuarto arreglo del catálogo general.

            break
        else:
            b = False  #Si no fue ninguno termina el ciclo.
    return  #No regresa nada al programa principal.


def leer_archivo(nombre_archivo):
    try:  #Verifica que exista el archivo.
        with open(nombre_archivo, 'r') as archivo:  #Abre el archivo solo en lectura.
            lineas = archivo.readlines()  #Lee el contenido por líneas.
        arreglo_diccionarios = []  #Crea el arreglo donde se guardaran los datos.
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
        respuesta_menu, b = opciones()  #Pedimos una especificación (pelicula, serie, etc.) y se verifica que sea válido.
        if 1 <= respuesta_menu <= 4:  #Si la respuesta está entre uno y cuatro.
            nombre_archivo = input('Ingresa el Nombre del archivo:\n')  #Pide el nombre del archivo a leer.
            catalogo[respuesta_menu - 1] = leer_archivo(nombre_archivo)  #Mandamos la información a una posición
                                                                         #especial del arreglo (1 es películas,
                                                                         #2 es series, 3 es documentales, etc.).
            break  #Terminamos el ciclo.
        else:  #De lo contrario.
            b = False  #Cerramos el ciclo.
    return catalogo  #Regresamos el catálogo general.


def mostrar_catalogo(catalogo):
    os.system('cls')  #Limpiar pantalla.
    b = True  #Inicializa el ciclo de verificación.
    while b:  #Ciclo de verificación.
        print('Mostrar Catalogo'.center(100, ' '))  #Mostramos un bonito título.
        respuesta, b = opciones()  #Pedimos una especificación (pelicula, serie, etc.) y se verifica que sea válido.
        if respuesta == 1:  #Si fue 1.
            pelicula_1 = catalogo[0]  #Ingresamos a una variable el primer arreglo del catalogo.
            mostrar(pelicula_1)  #Mostramos ese primer arreglo.
            time.sleep(8)  #Se queda quieta la pantalla por 8 segundos para mostrarlo.
        elif respuesta == 2:  #Si fue 2.
            serie_1 = catalogo[1]  #Ingresamos a una variable el segundo arreglo del catálogo.
            mostrar(serie_1)  #Mostramos ese segundo arreglo.
            time.sleep(8)  #Se queda quieta la pantalla por 8 segundos para mostrarlo.
        elif respuesta == 3:  #Si fue 3.
            documental_1 = catalogo[2]  #Ingresamos a una variable el tercer arreglo del catálogo.
            mostrar(documental_1)  #Mostramos ese tercer arreglo.
            time.sleep(8)  #Se queda quieta la pantalla por 8 segundos para mostrarlo.
        elif respuesta == 4:  #Si fue 4.
            evento_deportivo_1 = catalogo[3]  #Ingresamos a una variable el cuarto arreglo del catálogo.
            mostrar(evento_deportivo_1)  #Mostramos ese cuarto arreglo.
            time.sleep(8)  #Se queda quieta la pantalla por 8 segundos para mostrarlo.
        else:  #De lo contrario.
            b = False  #Se termina el ciclo.
    return  #No regresa nada al programa principal.


def eliminar_producto(catalogo_general):
    os.system('cls')  #Limpiar pantalla.
    print('Eliminar Producto'.center(100, ' '))  #Mostramos un bonito título.
    titulo = input('Ingresa el titulo que quieres eliminar.\n')  #Pedimos el título a eliminar.
    respuestas = buscar_producto(catalogo_general, titulo)  #Verificamos que ese título exista.
    if respuestas:  #Si existe ese diccionario.
        respuesta = input('Seguro quieres eliminarlo? [S/otra letra]\n').upper()  #Verificamos que ya encontrado
                                                                                  #realmente quiera eliminarlo.
        if respuesta == 'S':  #Si la respuesta fue "S".
            for i in catalogo_general:  #Buscamos dentro del primer arreglo.
                for i_2 in i:  #Buscamos en cada diccionario.
                    if [i_2] == respuestas:  #El diccionario que sea igual al anterior buscado.
                        i.remove(i_2)  #Se elimina.
                        print(f"Producto' {titulo} 'eliminado del catalogo.")  #Mostramos una leyenda de que se eliminó.
                        break  #Rompemos el ciclo.
        else:  #De lo contrario.
            return  #No hace nada.
    else:  #De lo contrario.
        print(f"No se encontró el producto '  {titulo}  'en el catálogo.")  #Decimos que no encontramos el producto a eliminar.
    return catalogo_general  #Regresamos el catálogo general al programa principal.


def buscar_producto(catalogo_general, palabras_clave):
    resultados = []  #Se crea un arreglo vacío donde ira el diccionario buscado.
    for producto in catalogo_general:  #Para cada arreglo del catálogo en general.
        for i in producto:  #Para cada diccionario dentro del arreglo.
            if palabras_clave in i:  #Buscamos coincidencias en los títulos.
                resultados.append(i)  #De haberlas se agrega ese diccionario al arreglo respuesta.
                break  #Se termina el ciclo.
            for i_2 in i:  #Para cada título.
                if palabras_clave in i_2:  #Buscamos coincidencias en los títulos.
                    resultados.append(i)  #De haberlas se agrega ese diccionario al arreglo respuesta.
                    break  #Se termina el ciclo.
                for i_3 in i[i_2]:  #Para cada contenido dentro del diccionario.
                    if palabras_clave in i_3:  #Buscamos coincidencias en el contenido del diccionario.
                        resultados.append(i)  #De haberlas se agrega ese diccionario al arreglo respuesta.
                        break  #Se termina el ciclo.
    if resultados:  #Si hubo resultados de la búsqueda.
        print("Resultados encontrados:", '\n')  #Mostramos una leyenda.
        mostrar(resultados)  #Y mostramos el resultado.
    else:  #De lo contrario.
        print("No se encontraron productos con las palabras clave proporcionadas.")  #Mostramos una leyenda.
    return resultados  #Regresamos esos resultados.


def agregar_evento():
    print('Evento deportivo'.center(100, ' '))  #Mostramos un bonito título.
    titulo = input('Ingresa el título del evento deportivo.\n')  #Pedimos el título.
    deporte = input('Ingresa deporte del que trata.\n')  #Pedimos el deporte.
    fecha = input('Ingresa el periodo anual de transmisión.\n')  #Pedimos el año. (no me deja poner año)
    hora = input('Ingresa la hora de transmisión.\n')  #Pedimos la hora de transmisión.
    lugar = input('Ingresa el lugar de donde se llevo acabo.\n')  #Pedimos el lugar.
    evento = {titulo: 'Deporte: ' + deporte + ' Periodo anual de lanzamiento: ' + fecha + ' Hora de transmisión: '
                      + hora + ' Lugar: ' + lugar}  #Creamos el diccionario.
    return evento  #Regresamos el diccionario al módulo agregar.


def agregar_documental():
    print('Documental'.center(100, ' '))  #Mostramos un bonito título.
    titulo = input('Ingresa el título del documental.\n')  #Pedimos el título.
    tema = input('Ingresa el tema del documental.\n')  #Pedimos el tema.
    director = input('Ingresa el director del documental.\n')  #Pedimos el director.
    fecha = input('Ingresa el periodo anual de lanzamiento del documental.\n')  #Pedimos el año. (no me deja poner año)
    documental = {titulo: 'Tema: ' + tema + ' Director: ' + director + ' Periodo anual lanzamiento: ' + fecha}  #Creamos diciconario.
    return documental  #Regresamos el diccionario al módulo agregar.


def agregar_serie():
    print('Serie'.center(100, ' '))  #Mostramos un bonito título.
    titulo = input('Ingresa el título de la serie.\n')  #Pedimos el título.
    actor = input('Ingresa el actor principal de la serie.\n')  #Pedimos el actor principal.
    director = input('Ingresa el director de la serie.\n')  #Pedimos el director.
    temporadas = input('Ingresa las temporadas de la serie.\n')  #Pedimos el número de temporadas.
    serie = {titulo: 'Actor principal: ' + actor + ' Temporadas: ' + temporadas + ' Director: ' + director}  #Creamos el diccionario.
    return serie  #Regresamos el diccionario al módulo agregar.


def agregar_peli():
    print('Pelicula'.center(100, ' '))  #Mostramos un bonito título.
    titulo = input('Ingresa el título de la película.\n')  #Pedimos el título.
    actor = input('Ingresa el actor principal de la película.\n')  #Pedimos el actor principal.
    fecha = input('Ingresa el periodo anual de lanzamiento de la película.\n')  #Pedimos el año. (no me deja poner año)
    director = input('Ingresa el director de la película.\n')  #Pedimos el director.
    peli = {titulo: 'Actor principal: ' + actor + ' Periodo anual de lanzamiento: ' + fecha + ' Director: ' + director}  #Creamos el diccionario.
    return peli  #Regresamos el diccionario al módulo agregar.


def agregar_producto(catalogo_general):
    respuesta_2 = 'S'
    respuesta = 'S'
    a = True            #Inicializamos ciclos.
    b = True
    while respuesta_2 == 'S':  #Ciclo para repetir o salir.
        os.system('cls')  #Limpiar pantalla.
        print('Agregar Producto'.center(100, ' '))  #Mostramos un bonito título.
        while b:  #Ciclo para verificar opciones.
            respuesta_2, b = opciones()  #Pedimos una especificación (pelicula, serie, etc.) y se verifica que sea válido.
            if respuesta_2 == 1:  #Si fue 1.
                while a:  #Ciclo para repetir proceso.
                    catalogo_general[0].append(agregar_peli())  #Agregamos el diccionario al arreglo en la posición 0.
                    a = regreso_ciclo()  #Verificación para saber si repetir.
                break  #Se termina el ciclo.
            elif respuesta_2 == 2:  #Si fue 2.
                while a:  #Ciclo para repetir proceso.
                    catalogo_general[1].append(agregar_serie())  #Agregamos el diccionario al arreglo en la posición 1.
                    a = regreso_ciclo()  #Verificación para saber si repetir.
                break  #Se termina el ciclo.
            elif respuesta_2 == 3:  #Si fue 3.
                while a:  #Ciclo para repetir proceso.
                    catalogo_general[2].append(agregar_documental())  #Agregamos el diccionario al arreglo en la posición 2.
                    a = regreso_ciclo()  #Verificación para saber si repetir.
                break  #Se termina el ciclo.
            elif respuesta_2 == 4:  #Si fue 4.
                while a:  #Ciclo para repetir proceso.
                    catalogo_general[3].append(agregar_evento())  #Agregamos el diccionario al arreglo en pa posición 3.
                    a = regreso_ciclo()  #Verificación para saber si repetir.
                break  #Se termina el ciclo.
            elif respuesta_2 == 5:  #Si fue 5.
                respuesta = 'S'  #Colocamos "s" en respuesta para mantener el programa principal.
                respuesta_2 = 'N'  #Colocamos "n" para cerrar esté módulo.
                break  #Se termina el ciclo.
    return catalogo_general, respuesta  #Regresamos el catálogo al programa principal junto a la respuesta.


def menu():
    print('Menu Principal'.center(100, ' '))  #Mostramos un bonito título.
    print('Seleccione la opción deseada'.center(100, ' '))
    print('='.center(100, '='))
    print('1.- Agregar Producto.')
    print('2.- Buscar Producto.')
    print('3.- Eliminar Producto.')   #Mostramos las opciones del programa principal.
    print('4.- Mostrar Catalogo.')
    print('5.- Cargar Catalogo.')
    print('6.- Guardar Catalogo.')
    print('7.- Salir.')
    while True:  #Ciclo de verificación.
        respuesta_menu = input('Ingrese el numero de opción que desea:\n')  #Pedimos ingrese una opción.
        if respuesta_menu.isdigit() and (1 <= int(respuesta_menu) <= 7):  #Si la respuesta fue un número y este entre 1 y 7.
            respuesta_menu = int(respuesta_menu)  #Convierte la respuesta en un entero.
            break  #Se termina el ciclo.
        else:  #De lo contrario.
            print('No es valido.')  #Mostramos una leyenda.
            continue  #Repetimos el proceso.
    return respuesta_menu  #regresamos la respuesta numerica al main.


def inicializar():
    respuesta = 'S'
    pelicula = []
    serie = []          #Inicializamos variables.
    documental = []
    evento_deportivo = []
    catalogo_general = [pelicula, serie, documental, evento_deportivo]
    return respuesta, catalogo_general  #Regresa la respuesta y el catálogo general.


def main():
    respuesta, catalogo_general = inicializar()  #Inicializamos las variables.
    while respuesta == 'S':  #Ciclo de proceso.
        a = True
        a_1 = True
        a_2 = True   #Inicializamos variables de proceso.
        a_3 = True
        a_4 = True
        os.system('cls')  #Limpiar pantalla.
        indice_menu = menu()  #Mostramos las opciones del menú y tomamos la elección.
        if indice_menu == 1:  #Si fue uno.
            while a:  #Ciclo para repetir proceso.
                catalogo_general, respuesta = agregar_producto(catalogo_general)  #Agregamos un producto, mandamos y recibimos el catálogo general.
                a = regreso_ciclo()  #Verificación para saber si repetir.
        elif indice_menu == 2:  #Si fue 2.
            while a_1:  #Ciclo para repetir proceso.
                os.system('cls')  #Limpiar pantalla.
                print('Buscar Producto'.center(100, ' '))  #Mostramos un bonito título.
                palabras_clave = input("Ingrese palabras clave para buscar un producto: \n")  #Pedimos palabras clave.
                buscar_producto(catalogo_general, palabras_clave)  #Buscamos el producto.
                a_1 = regreso_ciclo()  #Verificación para saber si repetir.
        elif indice_menu == 3:  #Si fue 3.
            while a_2:  #Ciclo para repetir proceso.
                catalogo_general = eliminar_producto(catalogo_general)  #Eliminamos un producto mandando y recibiendo el catálogo general.
                a_2 = regreso_ciclo()  #Verificación para saber si repetir.
        elif indice_menu == 4:  #Si fue 4.
            mostrar_catalogo(catalogo_general)  #Mostramos catálogo en especial.
        elif indice_menu == 5:  #Si fue 5.
            while a_3:  #Ciclo para repetir proceso.
                catalogo_general = cargar_catalogo(catalogo_general)  #Cargamos catálogo mandando y recibiendo el catálogo general.
                a_3 = regreso_ciclo()  #Verificación para saber si repetir.
        elif indice_menu == 6:  #Si fue 6.
            while a_4:  #Ciclo para repetir proceso.
                guardar_catalogo(catalogo_general)  #Guardamos catálogo en especial en un archivo.
                a_4 = regreso_ciclo()  #Verificación para saber si repetir.
        else:  #De lo contrario.
            respuesta = salir_prog()  #Verificamos si quiere salir del programa principal.


main()  #Llamamos al main.
