contadorpares = 0
contadorimpares = 0
contadorpositivos = 0
contadornegativos = 0
for c in range(0, 5):
    numeros = int(input())
    if numeros % 2 == 0:
        contadorpares += 1
    if numeros % 2 != 0:
        contadorimpares += 1
    if numeros > 0:
        contadorpositivos += 1
    if numeros < 0:
        contadornegativos += 1
print(f'{contadorpares} valor(es) par(es)')
print(f'{contadorimpares} valor(es) impar(es)')
print(f'{contadorpositivos} valor(es) positivo(s)')
print(f'{contadornegativos} valor(es) negativo(s)')
