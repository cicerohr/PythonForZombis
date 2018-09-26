def salva_transacao(preco: float, cartao_credito: int, descricao: str):
    """Abre o arquivo 'transacoes.txt' para escrever as informações das transações para enviar para o banco

    formato por linha: 0000090                 1234567890123456                        Pastel
                    preço(7 dígitos)     cartão de crédito(16 dígitos)  descrição do produto(16 caracteres)
    Obs.: preço está com formato bancário (0000090 ==> 0000090/100 = R$ 0,90).

    :param preco: preço do produto
    :type preco: float
    :param cartao_credito: número do cartão de crédito
    :type cartao_credito: int
    :param descricao: descrição do produto comprado
    :type descricao: str
    """
    file = open("transacoes.txt", "a", encoding="utf-8")
    file.write(f"{preco * 100:07.0f}{cartao_credito:16}{descricao:16}\n")
    file.close()
