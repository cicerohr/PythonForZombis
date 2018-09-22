# Faça um programa que leia quatro notas, mostre as notas e a média na tela.

notas = []
media = 0
print('-' * 30)
for c in range(0, 4):   # range([start], stop[, step]
    notas.append(float(input(f'Digite a {c + 1}ª nota: ')))
    media += notas[c]
print(f'Notas = {notas}')
print(f'A média das notas é {media / len(notas):.2f}.')
print('-' * 30)
