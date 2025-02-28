cod_quant = input()
codquant = cod_quant.split()
if codquant[0] == '1':
    print(f'Total: R$ {int(codquant[1]) * 4:.2f}')
else:
    if codquant[0] == '2':
        print(f'Total: R$ {int(codquant[1]) * 4.5:.2f}')
    else:
        if codquant[0] == '3':
            print(f'Total: R$ {int(codquant[1]) * 5:.2f}')
        else:
            if codquant[0] == '4':
                print(f'Total: R$ {int(codquant[1]) * 2:.2f}')
            else:
                if codquant[0] == '5':
                    print(f'Total: R$ {int(codquant[1]) * 1.5:.2f}')
