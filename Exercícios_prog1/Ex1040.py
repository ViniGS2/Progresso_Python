num = input()
numeros = num.split()
N1 = numeros[0]
N2 = numeros[1]
N3 = numeros[2]
N4 = numeros[3]
media = (float(N1) * 2 + float(N2) * 3 + float(N3) * 4 + float(N4) * 1) / (2 + 3 + 4 + 1)
if media >= 7.0:
    print(f'Media: {media:.1f}')
    print(f'Aluno aprovado.')

elif media < 5.0:
    print(f'Media: {media:.1f}')
    print(f'Aluno reprovado.')

else:
    print(f'Media: {media:.1f}')
    print(f'Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame}')
    mediafinal = (media + nota_exame) / 2
    if mediafinal >= 5.0:
        print(f'Aluno aprovado.')
        print(f'Media final: {mediafinal}')
    else:
        print(f'Aluno reprovado.')
        print(f'Media final: {mediafinal}')
