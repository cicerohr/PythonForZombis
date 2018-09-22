def eh_inteiro(entrada):
    """Verifica se o usuário digitou um número inteiro

    :param entrada: valor digitado pelo usuário
    :return: mensagem de erro ou a digitação do usuário
    """
    while True:
        try:
            entrada_usuario = int(input(entrada))
        except ValueError:
            print('Digite um número inteiro. Tente novamente!')
            continue
        else:
            return entrada_usuario
