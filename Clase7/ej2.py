"""Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que 
ha cumplido (desde 1 hasta su edad)."""

edad = int(input("Escriba su edad: "))

print("La cuenta de su edad seria: ")
for x in range(1, edad + 1):
    print(str(x) + " anos")
