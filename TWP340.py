# 1.1 - TWP340 Dicionários
# Dicionários, tipo para guardar dados de forma estruturada
from string import punctuation      # Importa os caracteres especias (!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~)

arq = open('alice.txt')             # Abre o arquivo com o texto do livro "Alice’s Adventures in Wonderland"
texto = arq.read()
texto = texto.lower()               # Coloca _todo o texto em letras minúsculas
for c in punctuation:
    texto = texto.replace(c, ' ')   # Substitui os caracteres especiais por espaço
texto = texto.split()               # Retorna uma lista usando espaço como delimitador
dic = {}
for p in texto:                     # Cria um dicionário para cada palavra e conta o número de ocorrência
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
print(f'Alice aparece {dic["alice"]} vezes.')
print('-' * 30)
print(dic)
arq.close()
