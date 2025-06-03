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
########
# cont=0
# total_dinero=0
# pago_mas_alto=[]
# try:
#     while True:
#         costo=int(input("""ingrese la opcion que desea
#                         1-full: 15.000$
#                         2-standart: 10.000$
#                         3-basico: 7.000$
#                         4-salir"""))
#         match costo:
#             case 1:
#                 while True:
#                     pago=int(input("ingrese su pago"))
#                     if pago>=15000:
#                         print(f"pago recibido, su vuelto es de {pago-15000}$")
#                         cont+=1
#                         total_dinero+=15000
#                         pago_mas_alto.append(pago)
#                         break
#                     else:
#                         print("pago insuficiente")
#             case 2:
#                 while True:
#                     pago=int(input("ingrese su pago"))
#                     if pago>=10000:
#                         print(f"pago recibido, su vuelto es de {pago-10000}$")
#                         cont+=1
#                         total_dinero+=10000
#                         pago_mas_alto.append(pago)
#                         break
#                     else:
#                         print("pago insuficiente")
#             case 3:
#                 while True:
#                     pago=int(input("ingrese su pago"))
#                     if pago>=7000:
#                         print(f"pago recibido, su vuelto es de {pago-7000}$")
#                         cont+=1
#                         total_dinero+=7000
#                         pago_mas_alto.append(pago)
#                         break
#                     else:
#                         print("pago insuficiente")
#             case 4:
#                 print("saliendo")
#                 break
# except Exception:
#     print("ingrese un numero entero")
# try:
#     print(f"los autos totales que ingresaron fue de {cont} autos y el total de dinero ganado es de {total_dinero}$")
#     print(f"el pago mas alto registrado fue de {max(pago_mas_alto)}")
# except Exception:
#     print("el numero de intentos fue 0")

#######
# cont = 0
# total_dinero = 0
# pagos_realizados = []

# while True:
#     try:
#         costo = int(input("""
# Ingrese la opción que desea:
#     1 - Full:     $15.000
#     2 - Standard: $10.000
#     3 - Básico:   $7.000
#     4 - Salir
# Opción: """))

#         if costo == 4:
#             print("Saliendo...")
#             break

#         if costo == 1:
#             precio = 15000
#         elif costo == 2:
#             precio = 10000
#         elif costo == 3:
#             precio = 7000
#         else:
#             print("Opción no válida.")
#             continue

#         while True:
#             pago = int(input("Ingrese su pago: "))
#             if pago >= precio:
#                 vuelto = pago - precio
#                 print(f"Pago recibido, su vuelto es de ${vuelto}")
#                 cont += 1
#                 total_dinero += precio
#                 pagos_realizados.append(pago)
#                 break
#             else:
#                 print("Pago insuficiente, intente de nuevo.")

#     except Exception:
#         print("Por favor, ingrese un número válido.")

# print(f"el Total de autos ingresados: {cont}")
# print(f"Total de dinero recaudado: ${total_dinero}")
# print(f"El pago más alto registrado fue: ${max(pagos_realizados)}")
##########
##########
# import random,time
# espada_diamante=0
# diamante=0
# palo=0
# carbon=0
# resta1=2
# resta2=1
# while True:
#     try:
#         op=int(input("""que desea hacer?
#                     1-minar
#                     2-craftear
#                     3-abrir el inventario
#                     4-salir"""))
#         match op:
#             case 1:
#                     minar=int(input("""que desea minar?
#                                     1-diamantes
#                                     2-palos"""))
#                     while True:
#                         match minar:
#                             case 1:
#                                 print("minando")
#                                 # time.sleep(3)
#                                 probabilidad=random.randint(1,7)
#                                 if probabilidad==1:
#                                     print("usted ha minado un diamante!!!")
#                                     diamante+=1
#                                 else:
#                                     print("usted consiguio un carbon")
#                                     carbon+=1
#                                 salir=int(input("""desea salir?
#                                                 1-si
#                                                 2-no"""))
#                                 match salir:
#                                     case 1:
#                                         print("saliendo")
#                                         break
#                             case 2:
#                                 print("minando")
#                                 # time.sleep(3)
#                                 probabilidad=random.randint(1,3)
#                                 if probabilidad==1:
#                                     print("usted ha minado un palo")
#                                     palo+=1
#                                 else:
#                                     print("consigui un carbon")
#                                     carbon+=1
#                                     salir=int(input("""desea salir?
#                                                 1-si
#                                                 2-no"""))
#                                 match salir:
#                                     case 1:
#                                         print("saliendo")
#                                         break
#             case 2:
#                 while True:
#                     print("necesita dos diamantes y un palo para craftear una espada")
#                     espada=int(input("""desea craftear una espada de diamante?
#                                     1-si
#                                     2-no"""))
#                     match op:
#                         case 1:
#                             if diamante<=1 or palo<=0:
#                                 print("usted no tiene recursos suficientes, consiga recursos para craftear una espada de diamante")
#                             elif diamante>=2 and palo>=1:
#                                 palo-=1
#                                 diamante-=2
#                                 print("usted ha crafteado una espada de diamante")
#                                 espada_diamante+=1
#                                 print(f"espada de diamante={espada_diamante}")
#                         case 2:
#                             print("saliendo")
#                             break
#             case 3:
#                 print(f"espada de diamante={espada_diamante}")
#                 print(f"diamantes={diamante}")
#                 print(f"palos={palo}")
#                 print(f"carbon={carbon}")
#             case 4:
#                 print("saliendo")
#                 break
#     except Exception:
#         print("ingrese una opcion valida")
############
############
# una farmacia donde sea por ticket aleatorio y muestre total de compras y total de tickets sacados y total ganados
# import random
# ganancias=[]
# total_compras=0
# total_usuario=0
# paracetamol=0
# dipirona=0
# algodon=0
# alcohol=0
# intento1=3
# intento2=3
# intento3=3
# nombre=str(input("ingrese su nombre "))
# while True:
#     try:
#         pase=int(input("ingrese su contraseña "))
#         break
#     except Exception:
#         print("solo debe contener numeros su contraseña")
# while True:
#     try:
#         rut=int(input("ingrese su rut sin puntos ni guiones "))
#         ticket=random.randint(1,400)
#         print(f"su ticket es el numero:{ticket}")
#         break
#     except Exception:
#         print("porfavor ingrese solo numeros, sin puntuacion ni letras")
# while True:
#     try:
#         total_usuario=0
#         op=int(input("""ingrese la opcion que desea
#                     1-menu de compras
#                     2-salir """))
#         match op:
#             case 1:
#                 try:
#                     while True:
#                         menu=int(input("""escoja la opcion que desea
#                                     1-paracetamol-1.500$
#                                     2-dipirona-3.000$
#                                     3-algodon-500$
#                                     4-alcohol-5.000$
#                                     5-pagar """))
#                         match menu:
#                             case 1:
#                                 paracetamol+=1500
#                                 total_compras+=1
#                                 ganancias.append(1500)
#                                 total_usuario+=1500
#                             case 2:
#                                 dipirona+=3000
#                                 total_compras+=1
#                                 ganancias.append(3000)
#                                 total_usuario+=3000
#                             case 3:
#                                 algodon+=500
#                                 total_compras+=1
#                                 ganancias.append(500)
#                                 total_usuario+=500
#                             case 4:
#                                 alcohol+=5000
#                                 total_compras+=1
#                                 ganancias.append(5000)
#                                 total_usuario+=5000
#                             case 5:
#                                 while True:
#                                     print(f"su total a pagar es de {total_usuario}")
#                                     rut2=int(input("ingrese su rut "))
#                                     if rut2==rut:
#                                         pase1=int(input("ingrese su contraseña "))
#                                         if pase1==pase:
#                                             pagar=int(input("ingrese el monto a pagar "))
#                                             if pagar>=total_usuario:
#                                                 print(f"perfecto, su vuelto es de {pagar-total_usuario}")
#                                                 print(f""" señor@ {nombre} su boleta es:
#                                                 nombre:{nombre}
#                                                 rut:{rut}
#                                                 total de productos comprados:{total_compras}
#                                                 monto a pagado {total_usuario}
#                                                 vuelto: {pagar-total_usuario}""")
#                                                 break
#                                             else:
#                                                 print("el monto que debe pagar debe ser igual o mayor al monto a pagar")
#                                                 intento1-=1
#                                                 print(f"intentos:{intento1}")
#                                                 if intento1==0:
#                                                     break
#                                         else:
#                                             ("contraseña incorrecta")
#                                             intento2-=1
#                                             print(f"intentos:{intento2}")
#                                             if intento2==0:
#                                                 break
#                                     else:
#                                         print("rut incorrecto")
#                                         intento3-=1
#                                         print(f"intentos:{intento3}")
#                                         if intento3==0:
#                                             break
#                                 break
#                             case _:
#                                 print("ingrese una opcion valida")
#                 except Exception:
#                     print("ingrese una opcion valida")    
#             case 2:
#                 print("saliendo")
#                 break
#     except Exception:
#         print("ingrese una opcion valida")
######
# import random
# maximo=[]
# noob=0
# normal=0
# pro=0
# while True:
#     try:
#         personas=int(input("cuantos niños buscaran hievitos de pascua"))
#         if personas<=0:
#             print("porfavor ingrese un numero positivo")
#         else:
#             break
#     except Exception:
#         print("ingrese solo numeros enteros porfavor")
# for i in range (personas):
#     huevos=random.randint(1,30)
#     print(f"el niño numero {i+1} consuguio {huevos} huevos")
#     maximo.append(huevos)
#     if huevos<=10:
#         print(f"el niño numero {i+1} es muy noob")
#         noob+=1
#     elif huevos>10 and huevos<=20:
#         print(f"el niño numero {i+1} lo hizo bien")
#         normal+=1
#     elif huevos>20:
#         print(f"el niño numero {i+1} es muy pro")
#         pro+=1
# print(f"""la cantidad de huevos mas alta encontrada es de {max(maximo)}
# la cantidad de niños noob {noob}
# la cantidad de niños que lo hicieron bien fue de {normal}
# la cantidad de niños que fueron pros fue de {pro}""")


# while True:
#     try:
#         cant_niños=int(input("Ingrese la cantidad de niños que participarán en la búsqueda de huevitos de pascua "))
#         while cant_niños<0:
#             print("Error, ingrese solo números positivos")
#             cant_niños=int(input("Ingrese la cantidad de niños que participarán en la búsqueda de huevitos de pascua "))
#         for i in range (cant_niños):
#             time.sleep(1)
#             print(f"Turno del niño n° {i+1}")
#             time.sleep(1)
#             cant_huevos=random.randint(3,30)
#             print(f"El niño n° {i+1} trajo {cant_huevos}")
#             if cant_huevos<12:
#                 print(f"El niño n° {i+1} es un Noob")
#                 noob+=1
#             elif cant_huevos>=12 and cant_huevos<=24:
#                 print(f"El niño n° {i+1} es un Master")
#                 Master+=1
#             else:
#                 print(f"El niño n° {i+1} es un Legend")
#                 legend+=1
#             if cant_huevos>top:
#                 top=cant_huevos
#         time.sleep(1)
#         print(f"La cantidad de Noobs es de {noob}")
#         print(f"La cantidad de Master es de {Master}")
#         print(f"La cantidad de Legend es de {legend}")
#         print(f"El mayor n° de huevos encontrados por un niño fue de {top}")
#         break
#     except Exception:
#         print("Solo debe ingresar números enteros")    
# total=0
# cantArt=0    

# while True:
#     try:
#         opcion=int(input(''' Carrito de compras
#                         Seleccione una opcion con un numero entero
#                         1.- Comprar Frutas
#                         2.- Comprar Verduras
#                         3.- Pagar
#                         4.- Salir
#                             '''))
#         match opcion:
#             case 1:
#                 while True:
#                     try:
#                         opcion=int(input('''
#                                         Seleccione una opcion con un numero entero
#                                         1.- Frutilla $1500
#                                         2.- Pera $1200
#                                         3.- Manzana $ 1300
#                                         4.- Volver al menu principal
#                                             '''))
#                         match opcion:
#                             case 1:
#                                 print("Has seleccionado Frutilla")
#                                 total+=1500
#                                 cantArt+=1
#                             case 2:
#                                 print("Has seleccionado Pera")
#                                 total+=1200
#                                 cantArt+=1
#                             case 3:
#                                 print("Has seleccionado Manzana")
#                                 total+=1300
#                                 cantArt+=1
#                             case 4:
#                                 print("Volviendo...")
#                                 break
#                             case _:
#                                 print("Opcion invalida")
#                     except Exception:
#                         print("Solo puede ingresar numeros enteros")   
#                     print(" TU total hasta ahora es ", total)
#             case 2:
#                 while True:
#                     try:
#                         opcion=int(input('''
#                                         Seleccione una opcion con un numero entero
#                                         1.- Papa $1500
#                                         2.- Lechuga $1200
#                                         3.- Cebolla $ 1300
#                                         4.- Volver al menu principal
#                                             '''))
#                         match opcion:
#                             case 1:
#                                 print("Has seleccionado Papa")
#                                 cant=int(input("Cuantas papas llevara?"))
#                                 total+=cant*1500
#                                 cantArt+=cant
#                             case 2:
#                                 print("Has seleccionado Lechuga")
#                                 total+=1200
#                                 cantArt+=1
#                             case 3:
#                                 print("Has seleccionado Cebolla")
#                                 total+=1300
#                                 cantArt+=1
#                             case 4:
#                                 print("Volviendo...")
#                                 break
#                             case _:
#                                 print("Opcion invalida")
#                     except Exception:
#                         print("Solo puede ingresar numeros enteros")   
#                     print(" TU total hasta ahora es ", total)
#             case 3:
#                 print("Has seleccionado pagar")
#                 print(f"El total de articulos es {cantArt}")
#                 print(f"El total a pagar es {total}")
#                 print(f"El total a pagar mas IVA es {round(total*1.19)}")
#             case 4:
#                 print("Saliendo...")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception:
#         print("Solo puede ingresar numeros enteros")       
####
# suma_alumno=0
# suma_curso=0
# while True:
#     try:
#         cant_alumnos=int(input("porfavor ingrese la cantidad totales de alumnos " ))
#         break
#     except Exception:
#         print("porfavor ingrese solo numeros")
# for i in range (cant_alumnos):
#     prom_alumno=0
#     suma_alumno=0
#     print(f"ingrese la cantidad de notas del alumno {i+1}" )
#     n_notas=int(input())
#     for n in range (n_notas):
#         notas=float(input(f"ingrese la nota numero {n+1} " ))
#         suma_alumno+=notas
#     prom_alumno=suma_alumno/n_notas
#     suma_curso+=prom_alumno
#     print(f"el promedio del alumno es {prom_alumno}" )
#     if prom_alumno>=4.0:
#         print("el alumno aprovo")
#     else:
#         print("el alumno desaprovo")
# print(f"el promedio del curso es {suma_curso/cant_alumnos}" )
#######
#######
# while True:
#     suma_promedios=0
#     try:
#         cant_alumn=int(input("Ingrese la cantidad de alumnos: "))
#         while cant_alumn<=0:
#             print("Solo debe ingresar números positivos")
#             cant_alumn=int(input("Ingrese la cantidad de alumnos: "))
#         for a in range (cant_alumn):
#             cant_notas=int(input(f"Ingrese la cantidad de notas del alumno {a+1}: "))
#             promedio=0
#             suma_notas=0
#             for p in range (cant_notas):
#                 nota=float(input(f"Ingrese la nota n° {p+1} del alumno {a+1}: "))
#                 suma_notas+=nota
#             promedio=suma_notas/cant_notas
#             if promedio>=4:
#                 print(f"El alumno {a+1} ha aprobado")
#             else:
#                 print(f"El alumno {a+1} ha reprobado")
#             suma_promedios+=promedio
#         promedio_general=suma_promedios/cant_alumn
#         print(f"El promedio general fue de {promedio_general}")
#         break
#     except Exception:
#         print("Solo debe ingresar números enteros o decimales en caso de las notas")
import os
from os import system
system("cls")
lista_prod=[]
while True:
    print("""
          1-agregar producto
          2-eliminar un producto
          3-listar productos
          4-salir del sistema""")
    op=int(input("->"))
    match op:
        case 1:
            producto=input("ingrese el producto que desea agregar")
            lista_prod.append(producto)
            print(f"el producto {producto}, fue agregado exitosamente")
            system("cls")
        case 2:
            cont = 1
            for i in lista_prod:
                print(f"{cont}.- {i}")
                cont+=1
            aux=int(input("eliminar ->"))-1
            print(f"producto {lista_prod[aux]} aliminado exitosamente")
            lista_prod.pop(aux)
            input("presione enter para continuar")
            system("cls")
        case 3:
            cont = 1
            for i in lista_prod:
                print(f"{cont}.-{i}")
                cont+=1
            print("presione enter para continuar")
            system("cls")
        case 4:
            print("saliendo del sistemaa")
            break
        case _:
            print("seleccion invalida, ingrese correctamente")














