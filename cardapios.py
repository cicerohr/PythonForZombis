from datetime import datetime


def chama_cardapio():
    """Dicionários com os cardapios de acordo com o periodos do dia
    Estrutura básica do dicionário:
                    dicionario = {item: [produto, preço]}
                                  int     str     float

    :return: dicionario com o cardápio
    """
    agora = str(datetime.now().time())[:5]
    if '06:00' < agora < '11:59':           # Manhã
        return {1: ["Bauru", 2.50], 2: ["X Salada", 3.0], 3: ["Calafrango", 2.20]}
    elif '12:00' < agora < '17:59':         # Tarde
        return {1: ["Esfiha", 1.50], 2: ["Coxinha", 2.20], 3: ["Pastel", 1.80], 4: ["Pão de Queijo", 1.20]}
    elif '18:00' < agora < '23:59':         # Noite
        return {1: ["Esfiha", 1.50], 2: ["Coxinha", 2.20], 3: ["Pastel", 1.80], 4: ["Pão de Queijo", 1.20]}
    else:                                   # Madrugada
        return {1: ["Esfiha", 1.50], 2: ["Coxinha", 2.20], 3: ["Pastel", 1.80], 4: ["Pão de Queijo", 1.20]}
