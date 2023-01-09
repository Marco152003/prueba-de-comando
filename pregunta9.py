# Un programa que verifique si la suma de 2 números es mayor,menor e igual que 20.
num1=float(input("Dame un número -> "))
num2=float(input("Dame otro número -> "))
if num1+num2>20:
   print("La suma de los 2 números es mayor que 20")
elif num1+num2<20:
   print("La suma de los 2 números es menor que 20")
else:
   print("La suma de los 2 números es igual que 20")