num = input().split()
a = int(num[0])
b = int(num[1])

if a >= b:
    c = a / b
else:
    c = b / a

if c == int(c):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
