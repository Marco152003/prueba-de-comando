# Hacer un programa que pida 2 números y se de cuenta cuál de ellos es par, o si ambos lo son.
num1 = int(input("Ingrese el num1 "))
num2 = int(input("Ingrese el num2 "))
if num1%2==0 and num2%2==0:
   print("Ambos números son pares")
elif num1%2==0 and num2%2!=0:
    print("Es par el ",num1)
elif num1%2!=0 and num2%2==0:
     print("Es par el número ",num2)   
elif num1%2!=0 and num2%2!=0:
     print("Los dos números son impares")