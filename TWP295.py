# 3.1 - TWP295 Módulo Random
# Módulos em Python, agrupando suas variáveis e funções.
from random import randint


def embaralha(self):
    """ Embaralha uma sequencia de string """
    from random import shuffle
    lista = list(self)
    shuffle(lista)
    return ''.join(lista)


def gerador_aleatorio():
    """ Gera uma lista com 15 inteiros aleatórios """
    from random import randint
    lista = []
    for i in range(15):
        lista.append(randint(10, 100))
    return lista


# Defina uma função "embaralha" que retorna as letras de uma string misturada.
# Dica: utilize list() para converter sua string em lista
print(embaralha('Grêmio'))

# Gere uma lista de 15 inteiros aleatório entre 10 e 100.
print(gerador_aleatorio())

# Gere uma lista de 15 inteiros aleatório entre 10 e 100 que sejam distintos entre si.
numeros = []
while len(numeros) < 15:
    numero = randint(10, 100)
    if numero not in numeros:
        numeros.append(numero)
numeros.sort()
print(numeros)
