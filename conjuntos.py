# Insertar nuevos conjuntos sin salir del programa.


def union_conjunto(conjunto_a,conjunto_b):

    print("\nLa únion de A y B es {}\n".format(conjunto_a.union(conjunto_b)))

def intersepcion_conjunto(conjunto_a,conjunto_b):

    print("\nLa intersepción de A y B es {}\n".format(conjunto_a.intersection(conjunto_b)))

def diferencia_simetrica(conjunto_a,conjunto_b):

    print("\nLa Diferencia Simetrica de A y B es {}\n".format(conjunto_a.symmetric_difference(conjunto_b)))


def diferencia_conjunto(conjunto_a,conjunto_b):
    print("Elige la diferencia que quieres realizar: ")
    print("1. A - B")
    print("2. B - A")

    try:

        operacion=int(input(": "))

    except ValueError:

        print("\nDebes introducir 1 o 2\n")
        diferencia_conjunto(conjunto_a,conjunto_b)

    else:

        if operacion == 1:

            print("\nLa diferencia de A - B es {}\n".format(conjunto_a.difference(conjunto_b)))

        elif operacion == 2:

            print("\nLa diferencia de B - A es {}\n".format(conjunto_b.difference(conjunto_a)))

        else :

            print("No reconosco esa Instrucción, Intenta de Nuevo!!!")

            diferencia_conjunto(conjunto_a,conjunto_b)


def ver_instrucciones():

    print("Operaciones que puedes realizar:")
    print("1 - Union\n2 - Intersección\n3 - Diferencia\n4 - Diferencia Simetrica\n5 - Volver a ver las Instrucciones\n6 - Salir.")

def calculadora_conjunto():

    print("Bienvenido a los Conjuntos")
    print("Introduce los elementos del conjunto por separado")
    print("Ejemplo: 1 2 3 4 5")

    conjunto_a=set(input("Conjunto A: ").split())
    conjunto_b=set(input("Conjunto B: ").split())


    ver_instrucciones()

    while True:
        try:
            operacion=int(input(": "))
        except ValueError:
            print("Introduce un numero del 1 al 6")

        else:

            if operacion == 1:
                union_conjunto(conjunto_a,conjunto_b)
            elif operacion == 2:
                intersepcion_conjunto(conjunto_a,conjunto_b)
            elif operacion == 3:
                diferencia_conjunto(conjunto_a,conjunto_b)
            elif operacion == 4:
                diferencia_simetrica(conjunto_a,conjunto_b)
            elif operacion == 5:
                ver_instrucciones()
            elif operacion == 6:
                break
            else:
                print("No reconosco esa Instrucción, Intenta de Nuevo!!!")


calculadora_conjunto()
print()
print("Gracias por utilizar la aplicación.")
