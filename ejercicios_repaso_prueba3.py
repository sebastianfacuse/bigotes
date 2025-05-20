# talleres=4
# while True:
#     try:
#         rojos=int(input("cuantos rojos hay en el curso"))
#         break
#     except Exception:
#         print("solo debe ingresar numeros enteros")
# while True:
#     try:
#         asistencia=int(input("""a cuantos talleres ah asistido?
#                             1-un solo taller
#                             2-dos talleres
#                             3-tres talleres
#                             4-cuatro talleres"""))
#         match asistencia:
#             case 1:
#                 print("usted recibe solo 0.3 decimas")
#                 print("usted no tiene la bendicion del profesor, asi que no se le puede ayudar")
#                 nota=float(input("ingrese la nota final"))
#                 nota+=0.3
#                 print(f"su nota mas las decimas acumuladas es un {nota}")
#                 break
#             case 2:
#                 print("usted recibe solo 0.6 decimas")
#                 print("usted no tiene la bendicion del profesor, asi que no se le puede ayudar")
#                 nota=float(input("ingrese la nota final"))
#                 nota+=0.6
#                 print(f"su nota mas las decimas acumuladas es un {nota}")
#                 break
#             case 3:
#                 print("usted recibe solo 0.9 decimas")
#                 print("usted no tiene la bendicion del profesor, asi que no se le puede ayudar")
#                 nota=float(input("ingrese la nota final"))
#                 nota+=0.9
#                 print(f"su nota mas las decimas acumuladas es un {nota}")
#                 break
#             case 4:
#                 print("usted recibe solo 1.2 decimas")
#                 print("usted tiene la bendicion del profesor")
#                 nota=float(input("ingrese la nota final"))
#                 nota+=1.2
#                 print(f"su nota mas las decimas acumuladas es un {nota}")
#                 break
#             case 5:
#                 print("diga la verdad alumno")
#     except Exception:
#         print("solo debe ingresar numeros")
# if nota>=4.0:
#     print("usted aprueba")
# else:
#     print("usted no aprueba")
# try:
#     op=int(input("ingrese un numero"))
# except Exception:
#     print("debe solo ingresar numeros enteros")
while True:
    costo=int(input("""ingrese la opcion que desea
                    1-full: 15.000$
                    2-standart: 10.000$
                    3-basico: 7.000$
                    4-salir"""))
    match costo:
        case 1:
            while True:
                pago=int(input("ingrese su pago"))
                if pago>=15000:
                    print(f"pago recibido, su vuelto es de {pago-15000}$")
                    break
                else:
                    print("pago insuficiente")
        case 2:
            while True:
                pago=int(input("ingrese su pago"))
                if pago>=10000:
                    print(f"pago recibido, su vuelto es de {pago-10000}$")
                    break
                else:
                    print("pago insuficiente")
        case 2:
            while True:
                pago=int(input("ingrese su pago"))
                if pago>=7000:
                    print(f"pago recibido, su vuelto es de {pago-7000}$")
                    break
                else:
                    print("pago insuficiente")
        case 4:
            print("saliendo")

