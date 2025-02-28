xy = input().split()
x = float(xy[0])
y = float(xy[1])

if x >= 0 and y > 0:
    if x == 0:
        print('Eixo Y')
    else:
        print('Q1')

if x < 0 and y >= 0:
    if y == 0:
        print('Eixo X')
    else:
        print('Q2')

if x <= 0 and y < 0:
    if x == 0:
        print('Eixo Y')
    else:
        print('Q3')

if x > 0 and y <= 0:
    if y == 0:
        print('Eixo X')
    else:
        print('Q4')

if x == 0 and y == 0:
    print('Origem')
