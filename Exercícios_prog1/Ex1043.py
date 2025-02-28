a_b_c = input().split()
a = float(a_b_c[0])
b = float(a_b_c[1])
c = float(a_b_c[2])
conta = abs(a - b)
trap = (a + b) * c / 2
if conta < c:
    print(f'Perimetro = {a+b+c:.1f}')
else:
    print(f'Area = {trap:.1f}')
