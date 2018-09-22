# 1.1 - TWP443 Módulos desconto fatec e japa
from banco import *
import descontos

itens = ["Esfiha", "Coxinha", "Pastel", "Pão de Queijo"]
precos = [1.50, 2.20, 1.80, 1.20]
print('-' * 45)
while True:
    opcao = 1
    for escolha in itens:
        print(f"{str(opcao)}. {escolha}")
        opcao += 1
    print(f"{str(opcao)}. Finalizar")
    print('-' * 15)
    escolha = int(input("Escolha uma opção: "))
    if escolha == opcao:
        # escolheu a última opção Finalizar
        print(' Fim '.center(45, '='))
        break
    else:
        cartao = input("Número do cartão de crédito: ")
        print('-' * 45)
        preco = descontos.desconto_10(precos[escolha - 1])
        if itens[escolha - 1] == "Pastel":
            preco = descontos.desconto_50(precos[escolha - 1])
        salva_transacao(preco, cartao, itens[escolha - 1])
