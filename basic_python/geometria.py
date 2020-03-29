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
