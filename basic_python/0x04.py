def modulo_C(z):
    j = abs(z)
    return j


dato = float(input("Por favor, ingresa el real: "))
modulo = float(input("Por favor, ingresa el imaginario: "))
z = complex(dato, modulo)
print("El modulo del numero complejo es: ", modulo_C(z))
