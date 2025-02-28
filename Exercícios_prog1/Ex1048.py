salario = float(input())
if salario <= 400.00:
    salmod = (salario * (15/100)) + salario
    print(f'Novo salario: {salmod:.2f}')
    print(f'Reajuste ganho: {salmod - salario:.2f}')
    print(f'Em percentual: 15 %')
if 400.00 < salario <= 800.00:
    salmod2 = (salario * (12/100)) + salario
    print(f'Novo salario: {salmod2:.2f}')
    print(f'Reajuste ganho: {salmod2 - salario:.2f}')
    print(f'Em percentual: 12 %')
if 800.00 < salario <= 1200.00:
    salmod3 = (salario * (10/100)) + salario
    print(f'Novo salario: {salmod3:.2f}')
    print(f'Reajuste ganho: {salmod3 - salario:.2f}')
    print(f'Em percentual: 10 %')
if 1200.00 < salario <= 2000.00:
    salmod3 = (salario * (7/100)) + salario
    print(f'Novo salario: {salmod3:.2f}')
    print(f'Reajuste ganho: {salmod3 - salario:.2f}')
    print(f'Em percentual: 7 %')
if salario > 2000.00:
    salmod4 = (salario * (4/100)) + salario
    print(f'Novo salario: {salmod4:.2f}')
    print(f'Reajuste ganho: {salmod4 - salario:.2f}')
    print(f'Em percentual: 4 %')
