import math


def area_triangulo(base, altura):
    j = ((base * altura)/2)
    return (j)


def area_circulo(t):
    j = (math.pi * (t ** 2))
    return (j)


base = float(input("Por favor, ingresa el primer lado: "))
altura = float(input("Por favor, ingresa el segundo lado: "))
print("El area del triangulo es:", area_triangulo(base, altura))
