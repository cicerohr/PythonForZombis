# 7.1 - TWP396 Revisão Listas cont

f = open('surf.txt')
notas = {}
for linha in f:
    nome, pontos = linha.split()
    notas[float(pontos)] = nome
f.close()
for nota in sorted(notas, reverse=True):
    print(f'{notas[nota]} tem nota {nota:4.2f}')
print(notas)
