salario = float(input())
slar_descont = salario - 2000.00
if slar_descont <= 0:
    print('Isento')
elif 0 < slar_descont <= 1000.00:
    print(f'R$ {slar_descont * (8 / 100):.2f}')
elif 1000.00 < slar_descont < 2000.00:
    slarmod = slar_descont // 1000
    print(f'R$ {((slarmod * 1000) * (8 / 100)) + ((slar_descont % 1000) * (18 / 100)):.2f}')
elif slar_descont > 2500.00:
    slar_descont28 = slar_descont - 2500
    print(f'R$ {(slar_descont28 * (28 / 100)) + (1500 * (18 / 100)) + (1000 * (8 / 100)):.2f}')
