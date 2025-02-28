contador = 0
soma = 0
for c in range(0, 6):
    numeros = float(input())
    if numeros > 0.0:
        contador += 1
        soma += numeros
        media = soma / contador



print(f'{contador} valores positivos')
print(f'{media:.1f}')
