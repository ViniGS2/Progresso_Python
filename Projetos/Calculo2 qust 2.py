'''Este programa necessita reconfiguração para troca de funções f(x)'''


# Sn

Xi = 1
Xf = 2
X = Xf - Xi
valor_da_alturaSn = 0
qunt_divisoes = int(input('Digite o valor de precisão: '))
valor_da_base = X / qunt_divisoes
resultadoSn = 0

# para saber a coordenadas novas de X e Y

for n in range(X, qunt_divisoes + 1):
    XnS = (n / qunt_divisoes) + Xi
    valor_da_alturaSn = 1 / XnS # linha da função
    resultadoSn += valor_da_alturaSn * valor_da_base

# sn

valor_da_alturasn = 0
resultadosn = 0

# para saber a coordenadas novas de X e Y

for n in range(Xi, qunt_divisoes):
    Xns = (n / qunt_divisoes) + Xi
    valor_da_alturasn = 1 / Xns # linha da função
    resultadosn += valor_da_alturasn * valor_da_base

print(f'{resultadosn} < A < {resultadoSn}')


# precisão 5 = 0.5456349206349207 < A < 0.6456349206349207
# precisão 10 = 0.6187714031754279 < A < 0.6687714031754279
# precisão 20 = 0.655803381792694 < A < 0.6808033817926941
# precisão 30 = 0.6682166153646801 < A < 0.6848832820313469
# precisão 50 = 0.6781721793101949 < A < 0.6881721793101949
# precisão 100 = 0.685653430481824 < A < 0.690653430481824
# precisão 1000 = 0.6923972430599377 < A < 0.6928972430599376
