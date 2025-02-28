A_B_C = input()
medidas = A_B_C.split()
pi = float(3.14159)
areatri = float(medidas[0]) * float(medidas[2]) / 2
areacirc = pi * float(medidas[2]) ** 2
areatrap = (float(medidas[0]) + float(medidas[1])) * float(medidas[2]) / 2
areaquadr = float(medidas[1]) ** 2
arearet = float(medidas[0]) * float(medidas[1])
print('TRIANGULO: {:.3f}'.format(areatri))
print('CIRCULO: {:.3f}'.format(areacirc))
print('TRAPEZIO: {:.3f}'.format(areatrap))
print('QUADRADO: {:.3f}'.format(areaquadr))
print('RETANGULO: {:.3f}'.format(arearet))
