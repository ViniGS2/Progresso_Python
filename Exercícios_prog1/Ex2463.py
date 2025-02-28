num_salas = int(input())
vidas_sala = input().split()
vidas_sala_num = []
vida_total = -100
testador = 0
for i in range(num_salas):
    vidas_sala_num.append(int(vidas_sala[i]))
for c in vidas_sala_num:
    testador += c
    if testador < 0:
        testador = 0
    if testador > vida_total:
        vida_total = testador

print(vida_total)
