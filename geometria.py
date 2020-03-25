import math


def area_triangulo(base, altura):
    j = ((base * altura)/2)
    return (j)


def area_circulo(t):
    j = (math.pi * (t ** 2))
    return (j)


def vol_esfera(f):
    i = ((4 * math.pi * (f**3))/3)
    return (i)


def vol_cilindro(r, h):
    i = (math.pi * (r**2) * h)
    return (i)


print("El area del triangulo es:", area_triangulo(5, 6))
print("El area del circulo es:", area_circulo(5))
print("El area de esfera es:", vol_esfera(5))
print("El area de cilindro es:", vol_cilindro(5, 3))
