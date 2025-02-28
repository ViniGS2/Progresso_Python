try:
    A_B_C = input().split()
    a = float(A_B_C[0])
    b = float(A_B_C[1])
    c = float(A_B_C[2])
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('Impossivel calcular')
    else:
        x1 = (-b + delta ** (1/2)) / (2 * a)
        x2 = (-b - delta ** (1/2)) / (2 * a)
        print(f'R1 = {x1:.5f}')
        print(f'R2 = {x2:.5f}')
except ZeroDivisionError:
    print('Impossivel calcular')