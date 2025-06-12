notas=[]
while True:
    while True:
        try:
            op=int(input("""que desea hacer???
                            1-ingresar nota
                            2-borrar nota
                            3-mostrar notas
                            4-sacar promedio, nota mayor y nota menor
                            5-limpiar todas las notas
                            6-salir
                            """))
            break
        except Exception:
            print("ingrese un numero entero valido")
    match op:
        case 1:
            cant_n=int(input("cuantas notas desea ingresar?? "))
            for i in range(cant_n):
                nota_n=float(input(f"ingrese la nota n {i+1} "))
                notas.append(nota_n)
        case 2:
            borrar=float(input("ingrese la nota que desea eliminar "))
            notas.remove(borrar)
            print("notas eliminadas")
        case 3:
            if len(notas)==0:
                print("no hay notas para mostrar")
            else:
                for a in range(len(notas)):
                    print(f"{a+1}- {notas[a]}") 
        case 4:
            try:
                print(f"el promedio es {sum(notas)/len(notas)}")
                print(f"la nota mayor es {max(notas)}")
                print(f"la nota menor es {min(notas)}")
            except Exception:
                print("las notas fueron eliminadas")
        case 5:
            print(".")
            print(".")
            print(".")
            notas.clear()
            print("notas eliminadas")
        case 6:
            print("saliendo")



