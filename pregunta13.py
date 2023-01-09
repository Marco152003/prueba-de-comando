#Calcular el nuevo salario de un profesor si gana segun el salario que se establesca.
salario =int(input("Ingrese el salario del profesor "))
if salario <1000:
   salario += (salario*0.12)
   print("El nuevo salario del profesor es ",salario)
elif 1000 <= salario <= 3000:
    salario += (salario*0.08)
    print("El nuevo salario del profesor es ",salario)
elif 3000 <= salario <= 5000:
    salario += (salario*0.07)
    print("El nuevo salario del profesor es ",salario)
else :
    salario += (salario*0.06)
    print("El nuevo salario del profesor es ",salario)