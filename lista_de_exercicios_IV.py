# Lista de Exercícios IV
#
from random import randint

print('-' * 30)
# 1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
# as funções max e min.
sorteio = list()
for k in range(10):
    sorteio.append(randint(1, 100))
sorteio.sort()
print(sorteio)
print(f'O maior valor {sorteio[-1]} e o menor valor é {sorteio[0]}.')
print('-' * 30)

# 2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
# números ímpares na lista IMPAR.
# Imprima as três listas.
sorteio = list()
pares = list()
impares = list()
for i in range(20):
    numero = randint(1, 100)
    sorteio.append(numero)
    if numero % 2 == 0:             # Verifica se é par
        pares.append(numero)
    else:
        impares.append(numero)
sorteio.sort()
pares.sort()
impares.sort()
print(sorteio)
print(f'Pares ({len(pares)}) ==> {pares}')
print(f'Ímpares ({len(impares)}) ==> {impares}')
print('-' * 30)

# 3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores. Imprima os três vetores.
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(10):
    v1 = randint(1, 100)
    v2 = randint(1, 100)
    vetor1.append(v1)
    vetor2.append(v2)
    vetor3.append(v1)
    vetor3.append(v2)
print(vetor1)
print(vetor2)
print(vetor3)
print('-' * 30)

# 4. Seja o statement sobre diversidade: “The Python Software Foundation and the global Python
# community welcome and encourage participation by everyone. Our community is based on
# mutual respect, tolerance, and encouragement, and we are working to help each other live up
# to these principles. We want our community to be more diverse: whoever you are, and
# whatever your background, we welcome you.”.
# Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou
# terminam com uma das letras “python”.
# Imprima a lista resultante.
# Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
alvo = ['P', 'p', 'Y', 'y', 'T', 't', 'H', 'h', 'O', 'o', 'N', 'n']
statement = 'The Python Software Foundation and the global Python community welcome and encourage participation by ' \
            'everyone Our community is based on mutual respect tolerance and encouragement and we are working to ' \
            'help each other live up to these principles We want our community to be more diverse whoever you are, ' \
            'and whatever your background we welcome you'
final = []
busca = statement.split()
for i in range(0, len(busca)):      # Varre a lista busca
    if busca[i][0] in alvo:         # Verifica s possui alguma letra (p y t h o n) no início da palavra
        final.append(busca[i])
    elif busca[i][-1] in alvo:      # Verifica s possui alguma letra (p y t h o n) no final da palavra
        final.append(busca[i])
print(busca)
print(len(busca))
print(final)
print(len(final))
print('-' * 30)

# 5. Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras
# “python” e que tenham mais de 4 caracteres.
# Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
alvo = ['p', 'y', 't', 'h', 'o', 'n']
objetivo = statement.lower().split()
final = []
print(objetivo)
for s in range(0, len(objetivo)):               # Varre a lista objetivo
    if len(objetivo[s]) > 4:                    # Verifica se a palavra, dentro da lista objetivo, tem mais de 4 letras
        cont = 0
        for h in range(0, len(objetivo[s])):    # Varre a palavra da lista objetivo
            if objetivo[s][h] in alvo:          # Busca pelas letras (p y t h o n) dentro da palavra
                cont += 1
        if cont > 0:
            final.append([objetivo[s], cont])   # Palavra encontrada; quantidade de letras (p y t h o n) encontradas
print(final)
print(f'Total de palavras que possui pelo menos uma letra da palavra "python": {len(final)}.')
print('-' * 30)
