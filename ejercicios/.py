# # nombre=input("ingrese un nombre")
# # for i in range (3):
# #     print("hola", nombre)
# notas=0
# print("bienvenido")
# for i in range (3):
#     nota=float(input("hola ingrese su nota"))
#     notas=notas+nota
# promedio=notas/3
# print("su promedio es", promedio)
## #ejercicion2
bonus_1=1.04
bonus_2=1.06
bonus_3=1.08
bonus_4=1000
bonus_5=2000
bonus_6=3000
sueldo=float(input("cual es su sueldo base? "))
sueldo_n2=sueldo+bonus_4 or bonus_5 or bonus_6
sueldo_total=sueldo_n2*bonus_1 or bonus_2 or bonus_3
lugar_en_tabla=int(input("¿en que lugar quedo su equipo esta temporada? "))
if lugar_en_tabla >=9:
    sueldo*bonus_4==sueldo_n2
    print(f"su sueldo esta temporada es {sueldo_n2}")
elif lugar_en_tabla >=4 and lugar_en_tabla <=8:
     sueldo*bonus_5==sueldo_n2
     print(f"su sueldo esta temporada es {sueldo_n2}")
elif lugar_en_tabla >=1 and lugar_en_tabla <=3:
     sueldo*bonus_6==sueldo_n2
     print(f"su sueldo esta temporada es {sueldo_n2}")
     #segunda parte
goles=int(input("cuantos goles marco esta temporada? "))
if goles>=1 and goles >=3:
    sueldo_n2*bonus_1==sueldo_total
    print(f"su sueldo total esta temporada es {sueldo_total}")
elif goles >=4 and goles <=6:
     sueldo_n2*bonus_2==sueldo_total
     print(f"su sueldo total esta temporada es {sueldo_total}")
elif goles >=7:
     sueldo_n2*bonus_3==sueldo_total
     print(f"su sueldo total esta temporada es {sueldo_total}")


# pida al usuario numero infinitamente y 
# muestre si son par o impar
# para salir, ponga 0 (cero).
# num=5
# while num!=0:
#     num=int(input("Ingrese un numero( cero para salir)"))
#     if num % 2==0:
#         print(f"El numero {num} es par")
#     else:
#         print(f"El numero {num} es impar")






































