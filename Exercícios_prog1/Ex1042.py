'''valores = input().split()
lista = [int(valores[0]), int(valores[1]), int(valores[2])]
for i in range(len(lista)):
    for c in range(0, len(lista) - 1):
        if lista[c] > lista[c + 1]:
            lista[c], lista[c + 1] = lista[c + 1], lista[c]
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}\n \n{valores[0]}\n{valores[1]}\n{valores[2]}')'''

'''valores = input().split()
lista = [int(valores[0]), int(valores[1]), int(valores[2])]
for i in range(0, 3):
    for c in range(0, 2):
        if lista[c] > lista[c + 1]:
            lista[c], lista[c + 1] = lista[c + 1], lista[c]
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}\n \n{valores[0]}\n{valores[1]}\n{valores[2]}')'''

valores = input().split()
lista1 = [int(valores[0]), int(valores[1]), int(valores[2])]
lista = [int(valores[0]), int(valores[1]), int(valores[2])]
lista.sort()
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')
print('')
print(f'{lista1[0]}\n{lista1[1]}\n{lista1[2]}')

