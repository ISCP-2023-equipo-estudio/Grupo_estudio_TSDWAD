from normativaBD import *
import datetime



bd= NormativaBD()
#bd.obtenerTipoNormativa()

def mostrarMenuPrincipal():
    print("\n+-------------------------------------------+")
    print("|        Leyes Vigentes CBA       |")
    print("+-------------------------------------------+\n")
    print("")
    print("MENÚ PRINCIPAL\n")
    print("[1] - INSERTAR")
    print("[2] - ELIMINAR")
    print("[3] - MOSTRAR")
    print("[4] - ACTUALIZAR")
    print("[5] - BUSCAR POR ID")
    print("[6] - BUSCAR POR PALABRAS CLAVE")
    print("[7] - SALIR")
    print("\n")

def insertarNuevaNormativa():
    print("--------Insertar nueva ley--------")
    idTipoNormativo = int(input("Ingrese el tipo de normativa"))
    nro_normativa = int(input("Ingrese el número de normativa"))
    fecha =  input("Ingrese la fecha de vigencia") #VER EL DATATIME
    descripcion = input("Ingrese la descripcíon de la ley")
    categoria = input("Ingrese la categoría")
    juridiccion = input("Ingrese la juridicción ")
    org_legislativo = input("Ingrese organo legislativo")
    palabras_clave = input("Ingrese palabras clave")
    bd.insertarNuevaNormativa()

def buscar_pclave():
    print("-------Buscar por palabras clave-----")
    palabras_clave = input("Ingresa las palabras clave separadas por comas: ")
    palabras_clave = [palabra.strip() for palabra in palabras_clave.split(",")]
    bd.buscar_pclave(palabras_clave)

def eliminarNormativa():
    print("--------Eliminar--------")
    bd.consultarNormativas()
    nroNormativa = input("Ingrese el numero de registro que desee eliminar")
    bd.eliminarNormativa(nroNormativa)


def crearMenuPrincipal():
    opcion = " "
    while (opcion != 7):
        mostrarMenuPrincipal()
        opcion = int(input("Ingrese su opción: "))
        
        if opcion == 1:
            insertarNuevaNormativa()
    
        elif opcion == 2:
           eliminarNormativa()


        elif opcion == 3:
            print()
        elif opcion == 4:
            print()
        elif opcion == 5:
            print("Saliendo...")
        else:
            print("Opción incorrecta")
      

def inicializar():
    crearMenuPrincipal()



inicializar()