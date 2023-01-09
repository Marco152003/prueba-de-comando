# Hallar el área y longitud de una circunferencia.
radio = float(input("Escribe el valor de radio "))
import math
longitud = 2*radio*math.pi
área = math.pi*radio**2
print("El valor de la longitud de la circunferencia es",longitud)
print("El valor del área de la circunferencia es",área)