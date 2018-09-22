# 1.1 - TWP440 Módulos


def salva_transacao(preco, cartao_credito, descricao):
    file = open("transacoes.txt", "a")
    # file.write("%16s%07d%16s\n" % (cartao_credito, preco * 100, descricao))
    file.write(f"{preco * 100:07.0f}{cartao_credito:16}{descricao:16}\n")
    file.close()


itens = ["Esfiha", "Coxinha", "Pastel", "Pão de Queijo"]
precos = [1.50, 2.20, 1.80, 1.20]
rodando = True
while rodando:
    opcao = 1
    for escolha in itens:
        print(f"{str(opcao)}. {escolha}")
        opcao += 1
    print(f"{str(opcao)}. Finalizar")
    escolha = int(input("Escolha uma opção: "))
    if escolha == opcao:
        # escolheu a última opção Finalizar
        rodando = False
    else:
        cartao = input("Número do cartão de crédito: ")
        salva_transacao(precos[escolha - 1], cartao, itens[escolha - 1])
print('-' * 30)
