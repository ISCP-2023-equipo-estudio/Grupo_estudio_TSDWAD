from normativaBD import *
from datetime import datetime



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
    print("[5] - BUSCAR POR NUMERO DE REGISTRO")
    print("[6] - BUSCAR POR PALABRAS CLAVE")
    print("[7] - SALIR")
    print("\n")

def insertarNuevaNormativa():
    print("--------Insertar nueva ley--------")
    bd.obtenerTipoNormativa()
    idTipoNormativa = int(input(f"Ingrese el tipo de normativa: "))
    nroNormativa = int(input("Ingrese el número de normativa: "))
    fecha =  datetime.strptime(input("Ingrese la fecha de vigencia formato: DD/MM/AAAA : "), '%d/%m/%Y').date()
    descripcion = input("Ingrese la descripcíon de la ley: ")
    bd.obtenerCategorias()
    categoria = input("Ingrese la categoría: ")
    bd.obtenerJurisdicciones()
    idTipoJurisdiccion = input("Ingrese la juridicción: ")
    palabrasClave = input("Ingrese palabras clave separadas por coma: ")
    bd.insertarNuevaNormativa(idTipoNormativa, nroNormativa, fecha, descripcion, categoria, idTipoJurisdiccion, palabrasClave  )


def eliminarNormativa():
    print("--------Eliminar--------")
    bd.consultarNormativas()
    nroNormativa = int(input("Ingrese el numero de registro que desee eliminar: "))
    bd.eliminarNormativa(nroNormativa)

def buscarPorNroNormativa ():
    nroNormativa = int(input("Ingrese un numero de registro: "))
    bd.obtenerNormativaPorNroNormativa(nroNormativa)



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
            buscarPorNroNormativa()
        elif opcion == 7:
            print("Saliendo...")
        else:
            print("Opción incorrecta")
      

def inicializar():
    crearMenuPrincipal()



inicializar()