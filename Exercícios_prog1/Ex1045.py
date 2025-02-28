numeros = input().split()
lista_float = [float(numeros[0]), float(numeros[1]), float(numeros[2])]
lista_float.sort(reverse=True)
if lista_float[0] >= lista_float[1] + lista_float[2]:
    print(f'NAO FORMA TRIANGULO')
else:
    if lista_float[0] ** 2 > lista_float[1] ** 2 + lista_float[2] ** 2:
        print(f'TRIANGULO OBTUSANGULO')
if lista_float[0] ** 2 == lista_float[1] ** 2 + lista_float[2] ** 2:
    print(f'TRIANGULO RETANGULO')
if lista_float[0] ** 2 < lista_float[1] ** 2 + lista_float[2] ** 2:
    print(f'TRIANGULO ACUTANGULO')
if lista_float[0] == lista_float[1] == lista_float[2]:
    print(f'TRIANGULO EQUILATERO')
if lista_float[0] == lista_float[1] != lista_float[2] or lista_float[0] == lista_float[2] != lista_float[1] or lista_float[1] == lista_float[2] != lista_float[0]:
    print(f'TRIANGULO ISOSCELES')
