cod1_num1_val1 = input()
peca1 = cod1_num1_val1.split()
cod2_num2_val2 = input()
peca2 = cod2_num2_val2.split()
pag1 = int(peca1[1]) * float(peca1[2])
pag2 = int(peca2[1]) * float(peca2[2])
pag = pag1 + pag2
print('VALOR A PAGAR: R$ {:.2f}'.format(pag))
