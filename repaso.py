# Calcular el araccel a pagar segun grupo familiar y comuna en la que reside
# A continuacion , los descuentos por cumuna:
# La Florida 20%, La pintana 30%, Puente Alto 25%, San Joaquin 15%
# Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%
# Preguntar al usuario en que comuna vive
# Preguntar al usuario con cuantas personas vive
# El arancel actual es de 200.000 por semestre  
# Basados en las respuestas del usuario  y en   
# la informacion dada, calcular su descuento
# comuna=0
# cont=0
# arancel=200000
# while comuna!=1 and comuna!=2 and comuna!=3 and comuna!=4 and comuna!=5:
#     print("""
#         1-la pintana
#         2-puente alto
#         3-la florida
#         4-san joaquin
#         5-otra comuna""")
#     comuna=int(input("ingrese su opcion"))
#     if comuna==1:
#         print("su descuento es del 30%")
#         cont+=30
#     elif comuna==2:
#         print("su descuento es del 25%")
#         cont+=25
#     elif comuna==3:
#         print("su descuento es del 20%")
#         cont+=20
#     elif comuna==4:
#         print("su descuento es del 15%")
#         cont+=20
#     elif comuna==5:
#         print("usted no tiene descuento")
#         cont+=0
# grupo=0
# while grupo!=1 and grupo!=2 and grupo!=3:
#     print("""
#         1-una persona
#         2-dos a cuatro personas
#         3-cinco personas o mas""")
#     grupo=int(input("ingrese su opcion"))
#     if grupo==1:
#         print("su descuento adicional es del 2%")
#         cont+=2
#     elif grupo==2:
#         print("su descuento adicional es del 3%")
#         cont+=3
#     elif grupo==3:
#         print("su descuento adicional es del 4%")
#         cont+=4
# print(f"el descuento total es del {cont}%")
# descuento_a=cont/100
# op=descuento_a*arancel
# print(f"el total a pagar es de {arancel-op} de {arancel}$")
# op=0
# arancel=200000
# descuento=0

# Designe 2 peleadores solicitando sus nombres
# cada peleador tiene 50 HP, debe mostrar la 
# barra de energia. Las peleas son por turnos #print("[]"*20)
# cada turno el peleador ataca entre 3 y 15
# Existe posibilidad de ataque critico del 20% sera atk*2
# gana el que le quita todo el HP al rival

# 
# hpj1=50
# hpj2=50
# import random
# turno=random.randint(1,2)
# import time

# while hpj1>0 and hpj2>0:
#     if turno % 2==0:
#         ataque=random.randint(3,15)
#         print("Turno del jugador 1")
#         time.sleep(1)
#         print("Jugador 1 ha atacado")
#         hpj2-=ataque
#         print(f"La vida del jugaror 2 bajado a bajado a {hpj2}")
#         time.sleep(1)
#     else:
#         ataque=random.randint(3,15)
#         print("Turno del jugador 2")
#         time.sleep(1)
#         print("Jugador 2 ha atacado")
#         hpj1-=ataque
#         print(f"La vida del jugaror 1 bajado a bajado a {hpj1}")
#         time.sleep(1)

#     turno+=1

# if hpj1>hpj2:
#     print("El ganador es el Jugador 1")
# else:
#     print("El ganador es el Jugador 2")
# comuna=0
# cont=0
# arancel=200000

# while comuna!=1 and comuna!=2 and comuna!=3 and comuna!=4 and comuna!=5:
#     comuna=int(input("indique de que comuna es" \
#     "                 1.- la florida " \
#     "                 2.- la pinatana" \
#     "                 3.- la granja" \
#     "                 4.- san joaquin"
#     "                 5.- otra comuna" \
#     "                 "))

#     if comuna==1:
#         print("su descuento es del 20%")
#         cont+=0.20
    
#     elif comuna==2:
#         print("su descuento es del 30%")
#         cont+=0.30
    
#     elif comuna==3:
#         print("su descuentos es del 25%")
#         cont+=0.25
    
#     elif comuna==4:
#         print("su descuento es del 15%")
#         cont+=0.15
#     elif comuna==5:
#         print("no tiene descuento")

    
# gp=0

# while gp!=1 and gp!=2 and gp!=3:
#  gp=int(input("indique con cuantas personas vive"
#  "              1.- 1 persona"
#  "              2.- 2 a 4 personas"
#  "              3.- 5 o mas personas"))

# if gp==1:
#   print("su descuento es del 2%")
#   cont+=0.02

# elif gp==2:
#    print("su descuento es del 3%")
#    cont+=0.03

# elif gp==3:
#    print("su descuento es del 4%")
#    cont+=0.04

# elif gp==4:
#    print("usted no tiene descuento")


# print(f"su descuento es de {cont*100}%")

# cont=1-cont
# arancel*=cont
 
# print(f" el total de su arancel es ${arancel}")



# # VOTATOON
# # Designe 2 cantdidatos. Pregunte cuanto votantes son
# # por cada votante , debe peguntar por quin votrá
# # cuente la cantidad de votos y muestre los resultados
# # definir quien ganó la votacion. Considere empate
boric=0
piñera=0
votantes=int(input("cuantos votantes son"))
for i in range (votantes):
    print("por quien votara?")
    print("1-bigotes")
    print("2-foppy")
    votos=int(input("ingrese su opcion"))
    if votos==1:
        boric+=1
    elif votos==2:
        piñera+=1
print(f"votos totales de foppy son= {boric}")
print(f"votos totales de bigotitos son= {piñera}")