"""Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo."""

numero = int(input("Escriba un numero entero positivo: "))


for x in range(1, numero + 1, 2):
    out = ""
    for y in range(x, 0, -2):
        out += str(y) + ", "  # out = out + str(y) + ", "
    print(out)
