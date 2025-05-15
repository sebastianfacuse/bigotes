# def credito():
#     comuna=0
#     cont=0
#     arancel=200000
#     while comuna!=1 and comuna!=2 and comuna!=3 and comuna!=4 and comuna!=5:
#         print("""
#             1-la pintana
#             2-puente alto
#             3-la florida
#             4-san joaquin
#             5-otra comuna""")
#         comuna=int(input("ingrese su opcion"))
#         if comuna==1:
#             print("su descuento es del 30%")
#             cont+=30
#         elif comuna==2:
#             print("su descuento es del 25%")
#             cont+=25
#         elif comuna==3:
#             print("su descuento es del 20%")
#             cont+=20
#         elif comuna==4:
#             print("su descuento es del 15%")
#             cont+=20
#         elif comuna==5:
#             print("usted no tiene descuento")
#             cont+=0
#     grupo=0
#     while grupo!=1 and grupo!=2 and grupo!=3:
#         print("""
#             1-una persona
#             2-dos a cuatro personas
#             3-cinco personas o mas""")
#         grupo=int(input("ingrese su opcion"))
#         if grupo==1:
#             print("su descuento adicional es del 2%")
#             cont+=2
#         elif grupo==2:
#             print("su descuento adicional es del 3%")
#             cont+=3
#         elif grupo==3:
#             print("su descuento adicional es del 4%")
#             cont+=4
#     print(f"el descuento total es del {cont}%")
#     descuento_a=cont/100
#     op=descuento_a*arancel
#     print(f"el total a pagar es de {arancel-op} de {arancel}$")
#     op=0
# def goles():
#     bonus_1=1.04
#     bonus_2=1.06
#     bonus_3=1.08
#     bonus_4=1000
#     bonus_5=2000
#     bonus_6=3000
#     sueldo=float(input("cual es su sueldo base? "))
#     sueldo_n2=sueldo+bonus_4 or bonus_5 or bonus_6
#     sueldo_total=sueldo_n2*bonus_1 or bonus_2 or bonus_3
#     lugar_en_tabla=int(input("¿en que lugar quedo su equipo esta temporada? "))
#     if lugar_en_tabla >=9:
#         sueldo*bonus_4==sueldo_n2
#         print(f"su sueldo esta temporada es {sueldo_n2}")
#     elif lugar_en_tabla >=4 and lugar_en_tabla <=8:
#         sueldo*bonus_5==sueldo_n2
#         print(f"su sueldo esta temporada es {sueldo_n2}")
#     elif lugar_en_tabla >=1 and lugar_en_tabla <=3:
#         sueldo*bonus_6==sueldo_n2
#         print(f"su sueldo esta temporada es {sueldo_n2}")
#         #segunda parte
#     goles=int(input("cuantos goles marco esta temporada? "))
#     if goles>=1 and goles >=3:
#         sueldo_n2*bonus_1==sueldo_total
#         print(f"su sueldo total esta temporada es {sueldo_total}")
#     elif goles >=4 and goles <=6:
#         sueldo_n2*bonus_2==sueldo_total
#         print(f"su sueldo total esta temporada es {sueldo_total}")
#     elif goles >=7:
#         sueldo_n2*bonus_3==sueldo_total
#         print(f"su sueldo total esta temporada es {sueldo_total}")
# def par_impar():
#     num=5
#     cont1=0
#     cont2=0
#     while num!=0:
#         num=int(input("ingrese un numero o presione 0 para salir"))
#         if num %2== 0:
#             print(f"su numero {num} es par")
#             cont1+=1
#             print(f"y la cantidad de numeros que ingreso es {cont1}")
#         else:
#             print(f"su numero {num} es inpar")
#             cont2+=1
#             print(f"y la cantidad de numeros que ingreso es {cont2}")
#     print(f"la cantidad de numeros totales es {cont1+cont2}")
# def menu():
#     while True:
#         op=int(input("""ingrese el programa que desea ejecutar
#                 1-credito
#                 2-goles
#                 3-numero par o impar
#                 4-salir"""))
#         match op:
#             case 1:
#                     credito()
#             case 2:
#                     goles()
#             case 3:
#                     par_impar()
#             case 4:
#                     print("saliendo")
#                     break
#             case _:
#                     print("opcion invalida")                                 
# menu()


# cont=0
# leche=200
# papas=300
# pan=500
# nombre=str(input("ingrese su nombre "))
# while True:
#     op=int(input("""grese la opcion que desea
#                 1-leche 200$
#                 2-papas 300$
#                 3-pan 500$
#                 4-salir"""))
#     match op:
#         case 1:
#             unt_leche=int(input("cuantas unidades desea llevar"))
#             cont+=unt_leche
#             leche*=unt_leche
#         case 2:
#             unt_papas=int(input("ingrese cuantas unidades de papa llevara"))
#             cont+=unt_papas
#             papas*=unt_papas
#         case 3:
#                  unt_pan=int(input("cuantos panes llevara"))
#                  cont+=unt_pan
#                  pan*=unt_pan
#         case 4:
#               if cont<3:
#                    print("la cantidad de unidades totales debe ser de 3 o mas unidades")
#               elif cont>=3:
#                    print(f"hola señor {nombre} su voleta es:")
#                    total=papas+leche+pan
#                    print(f"EL TOTAL NETO ES DE {total}")
#                    print(f"la cantidad de unidades totales que llevo es de {cont} y el total a pagar mas IVA es de {total*1.19}")
#                    break

suma_promedio=0
cantidad_de_alumnos=int(input("ingrese la cantidad de alumnos totales"))
for i in range (cantidad_de_alumnos):
     cantidad_notas=int(input("cuantas notas tiene el alumno?"))
     nota=0
     for e in range (cantidad_notas):
         nota=float(input("ingrese la nota"))
         nota+=nota
     promedio=nota/cantidad_notas
     if promedio<4:
          print(f"el alumno {i+1} esta desaprovado")
     else:
          print(f"el alumno {i+1} esta aprovado")
     suma_promedio+=promedio
promedio_general=suma_promedio/cantidad_de_alumnos
print(f"el promedio general es {promedio_general}")


    
     



                   

            

