def eh_inteiro(entrada: str) -> int:
    """Verifica se o usuário digitou um número inteiro

    :param entrada: valor digitado pelo usuário
    :type entrada: str
    :return: mensagem de erro ou a digitação do usuário
    :rtype: int
    """
    while True:
        try:
            entrada_usuario = int(input(entrada))
        except ValueError:
            print('Digite um número inteiro. Tente novamente!')
            continue
        else:
            return entrada_usuario
