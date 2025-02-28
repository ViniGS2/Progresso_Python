dias = int(input())
anos = dias // 365
dias_rest1 = dias % 365
meses = dias_rest1 // 30
dias_rest2 = dias_rest1 % 30
print(f'{anos} ano(s)\n{meses} mes(es)\n{dias_rest2} dia(s)')
