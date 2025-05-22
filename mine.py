import random,time
espada_diamante=0
diamante=0
palo=0
carbon=0
resta1=2
resta2=1
while True:
    try:
        op=int(input("""que desea hacer?
                    1-minar
                    2-craftear
                    3-abrir el inventario
                    4-salir"""))
        match op:
            case 1:
                    minar=int(input("""que desea minar?
                                    1-diamantes
                                    2-palos"""))
                    while True:
                        match minar:
                            case 1:
                                print("minando")
                                # time.sleep(3)
                                probabilidad=random.randint(1,7)
                                if probabilidad==1:
                                    print("usted ha minado un diamante!!!")
                                    diamante+=1
                                else:
                                    print("usted consiguio un carbon")
                                    carbon+=1
                                salir=int(input("""desea salir?
                                                1-si
                                                2-no"""))
                                match salir:
                                    case 1:
                                        print("saliendo")
                                        break
                            case 2:
                                print("minando")
                                # time.sleep(3)
                                probabilidad=random.randint(1,3)
                                if probabilidad==1:
                                    print("usted ha minado un palo")
                                    palo+=1
                                else:
                                    print("consigui un carbon")
                                    carbon+=1
                                    salir=int(input("""desea salir?
                                                1-si
                                                2-no"""))
                                match salir:
                                    case 1:
                                        print("saliendo")
                                        break
            case 2:
                while True:
                    print("necesita dos diamantes y un palo para craftear una espada")
                    espada=int(input("""desea craftear una espada de diamante?
                                    1-si
                                    2-no"""))
                    match espada:
                        case 1:
                            if diamante<=1 or palo<=0:
                                print("usted no tiene recursos suficientes, consiga recursos para craftear una espada de diamante")
                                break
                            elif diamante>=2 and palo>=1:
                                palo-=1
                                diamante-=2
                                print("usted ha crafteado una espada de diamante")
                                espada_diamante+=1
                                print(f"espada de diamante={espada_diamante}")
                        case 2:
                            print("saliendo")
                            break
            case 3:
                print(f"espada de diamante={espada_diamante}")
                print(f"diamantes={diamante}")
                print(f"palos={palo}")
                print(f"carbon={carbon}")
                while True:
                    cambio=int(input("""desea cambiar carbon por diamantes???
                                    1-si
                                    2-no"""))
                    match cambio:
                        case 1: 
                            if carbon>=10:
                                print("usted pudo cambiar carbon por diamantes!!!")
                                diamante+=1
                                carbon-=10
                                break
                            else:
                                print("no tiene suficientes carbones")
                                break
            case 4:
                print("saliendo")
                break
    except Exception:
        print("ingrese una opcion valida")
                        
