#Hacer un programa que pase de pulgadas a milimnetros y yardas a metros las millas a kilometros
opcion=int(input("***Menú*** /n1. pulgadas a milimetros /n2. yardas a metros /n3. millas a kilometros"))
if opcion==1:
    pulgadas=float(input("Dame el número de pulgadas "))
    milimetros=pulgadas* 25.40
    print("El numero de pulgadas en milimetros es ",milimetros)
elif opcion==2:
    yardas=float(input("Dame el número de yardas "))
    metros=yardas*0.9144
    print("El número de yardas a metros es ",metros)
elif opcion==3:
    millas=float(input("Dame el número de millas "))
    kilometros=millas*1.6093
    print("El número de millas en kilometros es ",kilometros)
else:
    print("El número que eligio no esta relacionado a las 3 opciones que se le da por favor vuelva intentarlo")