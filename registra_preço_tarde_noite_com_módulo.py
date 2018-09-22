from banco import *

itens = ["Esfiha", "Coxinha", "Pastel", "Pão de Queijo"]
precos = [1.50, 2.20, 1.80, 1.20]
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
