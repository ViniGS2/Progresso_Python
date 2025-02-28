filo = input()
classe = input()
alimentacao = input()
if filo == 'vertebrado':
    if classe == 'ave':
        if alimentacao == 'carnivoro':
            print('aguia')
        if alimentacao == 'onivoro':
            print('pomba')
    if classe == 'mamifero':
        if alimentacao == 'onivoro':
            print('homem')
        if alimentacao == 'herbivoro':
            print('vaca')

if filo == 'invertebrado':
    if classe == 'inseto':
        if alimentacao == 'hematofago':
            print('pulga')
        if alimentacao == 'herbivoro':
            print('lagarta')
    if classe == 'anelideo':
        if alimentacao == 'hematofago':
            print('sanguessuga')
        if alimentacao == 'onivoro':
            print('minhoca')