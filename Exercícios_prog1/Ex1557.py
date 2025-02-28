while True:
    tam_matr = int(input())
    if tam_matr == 0:
        break
    matriz = []
    for i in range(tam_matr):
        linha = [0] * tam_matr
        matriz.append(linha)
    for i in range(tam_matr):
        for c in range(tam_matr):
            matriz[i][c] = 2 ** (i + c)
    T = len(str(matriz[tam_matr-1][tam_matr-1]))
    for i in range(tam_matr):
        for c in range(tam_matr):
            matriz[i][c] = str(matriz[i][c])
            while len(matriz[i][c]) < T:
                matriz[i][c] = ' ' + matriz[i][c]
        m = ' '.join(matriz[i])
        print(m)
    print()