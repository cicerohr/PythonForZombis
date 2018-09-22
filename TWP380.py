# 5.1 - TWP380 Revisão Strings preço café

import urllib.request
from datetime import datetime
from time import sleep


def pega_preco():
    pagina = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
    texto = pagina.read().decode('utf8')
    onde = texto.find('>$')
    inicio = onde + 2
    fim = inicio + 4
    return float(texto[inicio:fim])


opcao = ' '
while opcao not in 'SN':
    opcao = str(input('Deseja comprar já? [S/N] '))[0].upper()
if opcao == 'S':
    preco = pega_preco()
    print(f'Comprar! Preço: $ {preco:5.2f} em {datetime.now()}')
else:
    preco = 99.99
    while preco >= 4.74:
        preco = pega_preco()
        if preco >= 4.74:
            print(f'Preço: $ {preco:5.2f} em {datetime.now()}')
            sleep(600)
    print(f'Comprar! Preço: $ {preco:5.2f} em {datetime.now()}')
