def mercado(lista, verificar):
    if ((verificar in lista) == True):
        return("Esta inluido")
    else:
        return("No esta incluido")


lista = ["huevos", "harina", "atun", "pescado", "arroz", "pan", "carne"]
verificar = str(input("Por favor, ingresa el alimento a verificar: "))
print("El producto  del mercado:", mercado(lista, verificar))
