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
personas={
    1:{"nombre": "liam nasson",
       "telefono": 569566066,
       "estado civil": "soltero",
       "ciudadano": True},
    2:{"nombre": "bigotes",
       "telefono": 56956656678,
       "estado civil": "casado",
       "ciudadano": True},
    3:{"nombre": "luka",
       "telefono": 569564577,
       "estado civil": "soltero",
       "ciudadano": False},
    4:{"nombre": "nicolas ñau",
       "telefono": 567893066,
       "estado civil": "divorsiado",
       "ciudadano": True},
}
while True:
        print("""
              1-ingresar persona
              2-mostrar listado
              3-actualizar persona
              4-borrar persona
              5-salir""")
        op=int(input("-> "))
        match op:
            case 1:
                nombre=str(input("ingrese el nombre de la persona que desea ingresar "))
                numero=int(input("ingrese el numero telefonico de la persona "))
                while True:
                    est_civil=int(input("""
                                        ingrese el estado civil de la persona:
                                        1-soltero
                                        2-casado
                                        """))
                    match est_civil:
                        case 1:
                            est_civil="Soltero"
                            break
                        case 2:
                            est_civil="Casado"
                            break
                        case _:
                            print("elija una opcion valida")
                while True:
                    ciud=int(input("""usted es ciudadano chileno???
                                    1-si
                                    2-no
                                """))
                    match ciud:
                        case 1:
                            ciud=True
                            break
                        case 2:
                            ciud=False
                            break
                        case _:
                            print("ingrese una opcion valida")
                Datos_Nuevos={"Nombre": nombre, "telefono": numero, "estado civil": est_civil, "ciudadano": ciud }
                personas[len(personas)+1]=Datos_Nuevos
            case 2:
                for n, persona in personas.items():
                    print(n, persona)
            case 3:
                for n, persona in personas.items():
                    print(n, persona)
                actualizar=int(input("""ingrese el numro de la persona que desea actualizar 
                                    -> """))
                if actualizar<=len(personas):
                    dato_a=int(input("""ingrese el dato que desea actualizar
                                     1- nombre
                                     2-numero
                                     3-estado civil
                                     4-ciudadania
                                    """))
                    match dato_a:
                        case 1:
                            nombre=str(input("ingrese el nombre de la persona que desea ingresar "))
                            personas[actualizar]["nombre"]=nombre
                        case 2:
                            numero=int(input("ingrese el numero telefonico de la persona "))
                            personas[actualizar]["telefono"]=numero
                        case 3:
                            while True:
                                est_civil=int(input("""
                                                    ingrese el estado civil de la persona:
                                                    1-soltero
                                                    2-casado
                                                    """))
                                match est_civil:
                                    case 1:
                                        est_civil="Soltero"
                                        break
                                    case 2:
                                        est_civil="Casado"
                                        break
                                    case _:
                                        print("elija una opcion valida")
                            personas[actualizar]["estado civil"]=est_civil
                        case 4:
                            while True:
                                ciud=int(input("""usted es ciudadano chileno???
                                                1-si
                                                2-no
                                            """))
                                match ciud:
                                    case 1:
                                        ciud=True
                                        break
                                    case 2:
                                        ciud=False
                                        break
                                    case _:
                                        print("ingrese una opcion valida")
                                personas[actualizar]["ciudadano"]=ciud
            case 4:
                # print(personas)
                for n, persona in personas.items():
                    print(n, persona)
                borrar=int(input("""ingrese el numero de la persona que desea eliminar
                                -> """))
                if borrar in personas:
                    personas.pop(borrar)
                else:
                    print("la persona no existe en la lista")
            case 5:
                print("saliendo...")
                break



# personas[3]["nombre"]=""