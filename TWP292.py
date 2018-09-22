# 2.1 - TWP292 Funções
# Funções, sua primeira entrada para reuso de código


def ehpar(x):
    """ Verifica se o número x é par """
    return x % 2 == 0


def fatorial(n):
    """ Fatorial de um número natural n """
    if n == 0 or n == 1:
        " Por definição 0! = 1 "
        return 1
    else:
        return n * fatorial(n - 1)


print(f'5 é par? {ehpar(5)}')
print(f'3! ==> 3 x 2 x 1 = {fatorial(3)}')
