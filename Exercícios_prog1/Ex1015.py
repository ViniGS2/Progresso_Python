x1y1 = input()
eixos1 = x1y1.split()
x2y2 = input()
eixos2 = x2y2.split()
x = (float(eixos2[0]) - float(eixos1[0])) ** 2
y = (float(eixos2[1]) - float(eixos1[1])) ** 2
dist = (x + y) ** (1/2)
print(f'{dist:.4f}')