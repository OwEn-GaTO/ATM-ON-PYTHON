import os 
os.system("cls")
print("\n")
saldo=1000
efectivo=1000
opc="0"

while opc!="4":
    pass
    
    print("\t.:menu:.")
    print("1.ingresar efectivo")
    print("2.retirar efectvo")
    print("3.mostrar saldo&efectivo")
    print("4.salir")
    opc=input("opccion: ")

    if opc=="1":
        ing=float(input("cantidad: "))
        print("\n")
        if 0<ing<=efectivo:
            saldo+=ing
            efectivo-=ing
            print(f"saldo: {saldo}\nefectivo: {efectivo}")
            print("\n\n\n")
        else:
            print("no tiene esa cantidad")
            print("\n\n\n")
    elif opc=="2":
        ret=float(input("cantidad: "))
        print("\n")
        if 0<ret<=saldo:
            efectivo+=ret
            saldo-=ret
            print(f"saldo: {saldo}\nefectivo: {efectivo}")
            print("\n\n\n")
        else:
            print("no tiene esa cantidad")
            print("\n\n\n")
    elif opc=="3":
        print(f"saldo: {saldo}\nefectivo: {efectivo}")
        print("\n\n\n")
    elif opc=="4":
        os.system("exit")

    else:
        print("seleccione una opccion valida")
        print("\n\n\n")

print("\n")
os.system("pause")