# Hallar la relación de 3 números.
num1 = float(input("Digite el primer numero -> "))
num2 = float(input("Digite el segundo numero -> "))
num3 = float(input("Digite el tercer numero -> "))

if num2<num1>num3:
          print("El primer numero insertado es el mayor ",num1)
elif num1<num2>num3:
          print("El segundo numero insertado es el mayor ",num2)
elif num1<num3>num2:
          print("El tercer numero insertado es el mayor ",num3)
elif num1==num2==num3:
        print("todos los números son iguales")