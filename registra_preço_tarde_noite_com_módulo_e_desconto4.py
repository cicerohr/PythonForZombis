# 1.1 - TWP443 Módulos desconto fatec e japa
from banco import salva_transacao
from descontos import desconto_10, desconto_50
from cardapios import chama_cardapio
from tratamento_erros import *

cardapio = chama_cardapio()
while True:
    print(' Cardápio '.upper().center(30, '-'))
    for k, v in cardapio.items():
        print(f'{k}. {v[0].ljust(18, ".")} R$ {v[1]:2.2f}')
    print('-' * 30)
    escolha = eh_inteiro("Escolha uma opção: [999. Sair] ")
    if escolha == 999:
        print(' Fim '.center(30, '='))
        break
    else:
        cartao = eh_inteiro("Número do cartão de crédito: ")
        preco = desconto_10(cardapio[escolha][1])
        if escolha == 3 and cardapio[escolha][0] == 'Pastel':
            preco = desconto_50(cardapio[escolha][1])
        salva_transacao(preco, cartao, cardapio[escolha][0])
        print('=' * 30)
        print(f'{cardapio[escolha][0]} desconto {int(100 - (100 * (preco / cardapio[escolha][1])))}%. R$ {preco:.2f}')
        print('=' * 30)
