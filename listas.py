# notas=[]
# while True:
#     while True:
#         try:
#             op=int(input("""que desea hacer???
#                             1-ingresar nota
#                             2-borrar nota
#                             3-mostrar notas
#                             4-sacar promedio, nota mayor y nota menor
#                             5-limpiar todas las notas
#                             6-salir
#                             """))
#             break
#         except Exception:
#             print("ingrese un numero entero valido")
#     match op:
#         case 1:
#             cant_n=int(input("cuantas notas desea ingresar?? "))
#             for i in range(cant_n):
#                 nota_n=float(input(f"ingrese la nota n {i+1} "))
#                 notas.append(nota_n)
#         case 2:
#             borrar=float(input("ingrese la nota que desea eliminar "))
#             notas.remove(borrar)
#             print("notas eliminadas")
#         case 3:
#             if len(notas)==0:
#                 print("no hay notas para mostrar")
#             else:
#                 for a in range(len(notas)):
#                     print(f"{a+1}- {notas[a]}") 
#         case 4:
#             try:
#                 print(f"el promedio es {sum(notas)/len(notas)}")
#                 print(f"la nota mayor es {max(notas)}")
#                 print(f"la nota menor es {min(notas)}")
#             except Exception:
#                 print("las notas fueron eliminadas")
#         case 5:
#             print(".")
#             print(".")
#             print(".")
#             notas.clear()
#             print("notas eliminadas")
#         case 6:
#             print("saliendo")
# def validar_code(code):
#     mayuscula=0
#     minuscula=0
#     digito=0
#     for palabra in code:
#         if palabra.isupper():
#             mayuscula+=1
#         if palabra.islower():
#             minuscula+=1
#         if palabra.isdigit():
#             digito+=1
#     if mayuscula==2 and minuscula==2 and digito==4:
#         print("el codigo esta bien")
#         return True
#     else:
#         print("el codigo esta mal escrito")
#     if validar_code(code):
#         personas[largo+1]={"nombre"= nombre,
#                            "telefono"= numero,
#                            "estado civil"= est_civil,
#                            "ciudadano"= ciud
#                             }
# personas={
#     1:{"nombre": "liam nasson",
#        "telefono": 569566066,
#        "estado civil": "soltero",
#        "ciudadano": True},
#     2:{"nombre": "bigotes",
#        "telefono": 56956656678,
#        "estado civil": "casado",
#        "ciudadano": True},
#     3:{"nombre": "luka",
#        "telefono": 569564577,
#        "estado civil": "soltero",
#        "ciudadano": False},
#     4:{"nombre": "nicolas ñau",
#        "telefono": 567893066,
#        "estado civil": "divorsiado",
#        "ciudadano": True},
# }
# while True:
#         print("""
#               1-ingresar persona
#               2-mostrar listado
#               3-actualizar persona
#               4-borrar persona
#               5-salir""")
#         op=int(input("-> "))
#         match op:
#             case 1:
#                 nombre=str(input("ingrese el nombre de la persona que desea ingresar "))
#                 numero=int(input("ingrese el numero telefonico de la persona "))
#                 while True:
#                     est_civil=int(input("""
#                                         ingrese el estado civil de la persona:
#                                         1-soltero
#                                         2-casado
#                                         """))
#                     match est_civil:
#                         case 1:
#                             est_civil="Soltero"
#                             break
#                         case 2:
#                             est_civil="Casado"
#                             break
#                         case _:
#                             print("elija una opcion valida")
#                 while True:
#                     ciud=int(input("""usted es ciudadano chileno???
#                                     1-si
#                                     2-no
#                                 """))
#                     match ciud:
#                         case 1:
#                             ciud=True
#                             break
#                         case 2:
#                             ciud=False
#                             break
#                         case _:
#                             print("ingrese una opcion valida")
#                 Datos_Nuevos={"Nombre": nombre, "telefono": numero, "estado civil": est_civil, "ciudadano": ciud }
#                 largo=list[personas.keys()][-1]
#                 personas.keys[largo+1]=Datos_Nuevos
#             case 2:
#                 for n, persona in personas.items():
#                     print(n, persona)
#             case 3:
#                 for n, persona in personas.items():
#                     print(n, persona)
#                 actualizar=int(input("""ingrese el numro de la persona que desea actualizar 
#                                     -> """))
#                 if actualizar<=len(personas):
#                     dato_a=int(input("""ingrese el dato que desea actualizar
#                                      1- nombre
#                                      2-numero
#                                      3-estado civil
#                                      4-ciudadania
#                                     """))
#                     match dato_a:
#                         case 1:
#                             nombre=str(input("ingrese el nombre de la persona que desea ingresar "))
#                             personas[actualizar]["nombre"]=nombre
#                         case 2:
#                             numero=int(input("ingrese el numero telefonico de la persona "))
#                             personas[actualizar]["telefono"]=numero
#                         case 3:
#                             while True:
#                                 est_civil=int(input("""
#                                                     ingrese el estado civil de la persona:
#                                                     1-soltero
#                                                     2-casado
#                                                     """))
#                                 match est_civil:
#                                     case 1:
#                                         est_civil="Soltero"
#                                         break
#                                     case 2:
#                                         est_civil="Casado"
#                                         break
#                                     case _:
#                                         print("elija una opcion valida")
#                             personas[actualizar]["estado civil"]=est_civil
#                         case 4:
#                             while True:
#                                 ciud=int(input("""usted es ciudadano chileno???
#                                                 1-si
#                                                 2-no
#                                             """))
#                                 match ciud:
#                                     case 1:
#                                         ciud=True
#                                         break
#                                     case 2:
#                                         ciud=False
#                                         break
#                                     case _:
#                                         print("ingrese una opcion valida")
#                                 personas[actualizar]["ciudadano"]=ciud
#             case 4:
#                 # print(personas)
#                 for n, persona in personas.items():
#                     print(n, persona)
#                 borrar=int(input("""ingrese el numero de la persona que desea eliminar
#                                 -> """))
#                 if borrar in personas:
#                     personas.pop(borrar)
#                 else:
#                     print("la persona no existe en la lista")
#             case 5:
#                 print("saliendo...")
#                 break

# largo=list[juegos.keys()][-1]
# juegos.keys[largo+1]=Datos_Nuevos
# personas[3]["nombre"]=""
# def validar_code(code):
def mostrar(juegos):
    for i, n in juegos.items():
        print(i,n)
juegos={
    1: {"nombre": " dayligby hdeadt",
       "precio": 2000,
       "codigo": "t456"},
    2: {"nombre": "gta 5",
        "precio": 2500,
        "codigo": "ht56"},
    3: {"nombre": "fifa 2025",
        "precio": 5000,
        "codigo": "gt11"}
}
while True:
    print("""
          1-ingresar juego
          2-actualizar juego
          3-borrar juego
          4-mostrar juego
          5-salir""")
    op=int(input("ingrese la opcion que desea "))
    match op:
        case 1:
            nombre=input("ingresa el nombre del juego que vas a igresar")
            precio=input("ingrese el precio del juego")
            codigo=input("ingrese el codigo del juego")
            largo=list(juegos.keys())[-1]
            juegos[largo+1]={
                "nombre": nombre,
                "precio": precio,
                "codigo": codigo,
            }
        case 2:
            print(mostrar(juegos))
            act=int(input("ingrese el numero del juego que desea actualizar -> "))
            if act in juegos:
                print(mostrar(juegos))
                print("""
                        1-nombre
                        2-precio
                        3-codigo""")
                act1=int(input("ingrese lo que desea actualizar "))
                match act1:
                    case 1:
                        nom=input("ingrese el nombre que desea ")
                        juegos[act]["nombre"]= nom
                    case 2:
                        prec=input("ingrese el precio nuevo ")
                        juegos[act]["precio"]= prec
                    case 3:
                        cod=input("ingrese el codigo nuevo ")
                        juegos[act]["codigo"]= cod
        case 3:
            mostrar(juegos)
            borrar=int(input("ingrese el numero del juego que desea eliminar "))
            if borrar in juegos:
                del juegos[borrar]
                print("juego borrado con exito")
            else:
                print("el juego no se encuentra dentro de la lista")
        case 4:
            mostrar(juegos)
        case 5:
            print("saliendo...")
            break      


