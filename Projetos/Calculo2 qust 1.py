'''Este programa necessita reconfiguração para troca de funções f(x)'''

# Sn

Xi = 0
Xf = 1
X = Xf - Xi # serve para saber quanto valerá cada parte
valor_da_alturaSn = 0
qunt_divisoes = int(input('Digite o valor de precisão: '))
valor_da_base = X / qunt_divisoes
resultadoSn = 0

# para saber a coordenadas novas de X e Y

for n in range(X, qunt_divisoes + 1):
    Xn = (n / qunt_divisoes) + Xi
    valor_da_alturaSn = (Xn ** 2) # linha da função
    resultadoSn += valor_da_alturaSn * valor_da_base

# sn

valor_da_altura = 0
valor_da_base = X / qunt_divisoes
resultadosn = 0

# para saber a coordenadas novas de X e Y

for n in range(Xi, qunt_divisoes):
    Xn = (n / qunt_divisoes) + Xi
    valor_da_altura = (Xn ** 2) # linha da função
    resultadosn += valor_da_altura * valor_da_base

print(f'{resultadosn} < A < {resultadoSn}')

# precisão 4 = 0.21875 < A < 0.46875
# precisão 10 = 0.28500000000000003 < A < 0.385
# precisão 20 = 0.30874999999999997 < A < 0.35874999999999996
# precisão 30 = 0.3168518518518519 < A < 0.3501851851851852
# precisão 50 = 0.3234 < A < 0.34340000000000004
# precisão 100 = 0.32835000000000014 < A < 0.33835000000000015
# precisão 1000 = 0.3328335000000003 < A < 0.3338335000000003

