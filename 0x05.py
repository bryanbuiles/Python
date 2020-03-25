lado1 = float(input("Por favor, ingresa el primer lado: "))
lado2 = float(input("Por favor, ingresa el segundo lado: "))
lado3 = float(input("Por favor, ingresa el tercer lado: "))


def a_triangulo(lado1, lado2, lado3):
    j = ((float(lado1 + lado2 + lado3)/2))
    return ((j*(j-lado1)*(j-lado2)*(j-lado3))**0.5)


print("El area del triangulo es:", a_triangulo(lado1, lado2, lado3))
