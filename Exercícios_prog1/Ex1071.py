x = int(input())
y = int(input())
soma = 0
if y > x:
    for c in range(x + 1, y):
        if c % 2 != 0:
            soma += c
elif y < x:
    for i in range(y + 1, x):
        if i % 2 != 0:
            soma += i
print(soma)
