nome = input()
salariofixo = float(input())
vendmes = float(input())
comissao = vendmes * 0.15
salario = salariofixo + comissao
print('TOTAL = R$ {:.2f}'.format(salario))