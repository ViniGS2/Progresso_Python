from random import randint
num = randint(1, 10)
adinhação = 0
while adinhação != num:
    adivinhação = int(input('Digite um número de 1 a 10: '))
    if adivinhação == num:
        print('Você ganhou!')
        break
    if adivinhação > num:
        print('Muito alto!')
    if adivinhação < num:
        print('Muito baixo!')