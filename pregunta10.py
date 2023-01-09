# Hacer un programa que indique si un num1 elevado al num2 es mayor,menor e igual que 1000.
num1=float(input("El valor de num1 es -> "))
num2=float(input("El valor de num2 es -> "))
if num1**num2>1000:
   print("El num1 elevado al num2 es mayor que 1000")
elif num1**num2<1000:
    print("El num1 elevado al num2 es menor que 1000")
else:
    print("El num1 elevado al num2 es igual que 1000")