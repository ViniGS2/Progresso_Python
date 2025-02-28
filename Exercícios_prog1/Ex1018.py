valor = int(input())
print(valor)
print(f'{valor // 100} nota(s) de R$ 100,00')
valor2 = valor % 100
print(f'{valor2 // 50} nota(s) de R$ 50,00')
valor3 = valor2 % 50
print(f'{valor3 // 20} nota(s) de R$ 20,00')
valor4 = valor3 % 20
print(f'{valor4 // 10} nota(s) de R$ 10,00')
valor5 = valor4 % 10
print(f'{valor5 // 5} nota(s) de R$ 5,00')
valor6 = valor5 % 5
print(f'{valor6 // 2} nota(s) de R$ 2,00')
valor7 = valor6 % 2
print(f'{valor7 // 1} nota(s) de R$ 1,00')