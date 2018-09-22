from banco import *

itens = ["Bauru", "X Salada", "Calafrango"]
precos = [2.50, 3.0, 2.20]
rodando = True

while rodando:
    opcao = 1
    for escolha in itens:
        print(f"{str(opcao)}. {escolha}")
        opcao = opcao + 1
    print(f"{str(opcao)}. Finalizar")
    escolha = int(input("Escolha uma opção: "))
    if escolha == opcao:
        # escolheu a última opção Finalizar
        rodando = False
    else:
        cartao = input("Número do cartão de crédito: ")
        salva_transacao(precos[escolha - 1], cartao, itens[escolha - 1])
