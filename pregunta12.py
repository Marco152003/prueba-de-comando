#Hacer un programa que funcione como una caja bancaria en la cual podremos retirar, añadir y mostrar el saldo.
saldo = int(1000)

anuncio = input("Eliga una de las opciones: \n1.Ingresar dinero\n2.Retirar Dinero\n3.Mostrar dinero disponible\n4.Salir\n")

if anuncio == '1' :
    num = int(input("Monto que desee ingresar: "))
    total = saldo + num
    print(f"su saldo total es de {total}")
elif anuncio == '2' :
    num = int(input("Monto que desee Retirar: "))
    if 0 < num < 1000 :
        total = saldo - num
        print(f"su saldo total es de: {total}")
    else :
        print("Saldo insuficiente")

elif anuncio == '3' :
    print(f"Su dinero disponible es de {saldo}")

elif anuncio == '4' :
    print("Fin del programa")