# bonus_1=1.04
# bonus_2=1.06
# bonus_3=1.08
# bonus_4=1000
# bonus_5=2000
# bonus_6=3000
# sueldo=float(input("cual es su sueldo base? "))
# sueldo_n2=sueldo+bonus_4 or bonus_5 or bonus_6
# sueldo_total=sueldo_n2*bonus_1 or bonus_2 or bonus_3
# lugar_en_tabla=int(input("¿en que lugar quedo su equipo esta temporada? "))
# if lugar_en_tabla >=9:
#     sueldo*bonus_4==sueldo_n2
#     print(f"su sueldo esta temporada es {sueldo_n2}")
# elif lugar_en_tabla >=4 and lugar_en_tabla <=8:
#      sueldo*bonus_5==sueldo_n2
#      print(f"su sueldo esta temporada es {sueldo_n2}")
# elif lugar_en_tabla >=1 and lugar_en_tabla <=3:
#      sueldo*bonus_6==sueldo_n2
#      print(f"su sueldo esta temporada es {sueldo_n2}")
#      #segunda parte
# goles=int(input("cuantos goles marco esta temporada? "))
# if goles>=1 and goles >=3:
#     sueldo_n2*bonus_1==sueldo_total
#     print(f"su sueldo total esta temporada es {sueldo_total}")
# elif goles >=4 and goles <=6:
#      sueldo_n2*bonus_2==sueldo_total
#      print(f"su sueldo total esta temporada es {sueldo_total}")
# elif goles >=7:
#      sueldo_n2*bonus_3==sueldo_total
#      print(f"su sueldo total esta temporada es {sueldo_total}")
# num=5
# cont1=0
# cont2=0
# while num!=0:
#      num=int(input("ingrese un numero o presione 0 para salir"))
#      if num %2== 0:
#           print(f"su numero {num} es par")
#           cont1+=1
#           print(f"y la cantidad de numeros que ingreso es {cont1}")
#      else:
#           print(f"su numero {num} es inpar")
#           cont2+=1
#           print(f"y la cantidad de numeros que ingreso es {cont2}")
# print(f"la cantidad de numeros totales es {cont1+cont2}")

 ##BATALLA POKEMON

hp_pokemon1=50
hp_pokemon2=50
pokemon1=str(input("ingrese el nombre de su pokemon"))
pokemon2=str(input("ingrese el nombre de su pokemon"))
while hp_pokemon1 or hp_pokemon2!=0:
    print(f"turno de {pokemon1}")
    