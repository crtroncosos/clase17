from os import system
lista_trabajador:{""}
def menu_principal():
    opciones = {
        '1': ('Registrar Trabajador', registrar_trabajador),
        '2': ('Listar todos los trabajadores ', lis_trabajadores),
        '3': ('Imprimir planilla de sueldos', sueldos),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        system("cls")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def registrar_trabajador():
    system("cls")
    nombre = input("Ingrese nombre y apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador: ")
    sueldo_bruto = int(input("Ingrese el sueldo bruto del trabajador: "))
    desc_salud = int(round(sueldo_bruto * 7/100,0))
    desc_afp = int(round(sueldo_bruto * 12/100,0))
    liquido = sueldo_bruto - desc_salud - desc_afp
    lista_trabajador.append({
                    "Nombres": nombre,
                    "Cargo" : cargo,
                    "sueldo_bruto" : sueldo_bruto,
                    "desc_salud" : desc_salud,
                    "desc_afp" : desc_afp,
                    "liquido" : liquido,
                })
    
    print(lista_trabajador)
    input()
    return


def lis_trabajadores():
    print('Listar Todos los Trabajadores')


def sueldos():
    print('Imprimir planilla de sueldos')


def salir():
    print('Saliendo del programa')


menu_principal()