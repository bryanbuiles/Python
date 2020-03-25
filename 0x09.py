def listdic(diccionario, verificar):

    if verificar in diccionario:
        return(diccionario[verificar])
    else:
        return("ausente")


diccionario = {1: "Alberto", 2: "Jose", 3: "Bryan"}
verificar = int(input("Por favor, ingresa un numero: "))
print("El nombre de la persona es:", listdic(diccionario, verificar))
