tempo = int(input())
vel_media = int(input())
dist_percorrida = tempo * vel_media
gasto_combust = dist_percorrida / 12
print(f'{gasto_combust:.3f}')