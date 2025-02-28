a_b_c = input()
valores = a_b_c.split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])
maior = (a + b +abs(a-b)) / 2
maiores = int(maior)
if maiores >= c:
    print(f'{maiores} eh o maior')
else:
    print(f'{c} eh o maior')
