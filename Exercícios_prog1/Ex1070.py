numero = int(input())
if numero % 2 ==0:
    for c in range(numero, numero + 12):
        if c % 2 != 0:
            print(f'{c}')
elif numero % 2 != 0:
    for i in range(numero, numero + 11):
        if i % 2 != 0:
            print(f'{i}')
