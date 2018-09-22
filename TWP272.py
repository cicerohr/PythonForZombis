# 1.1 - TWP272 Ler um vetor
# Nesta aula aprenderemos sobre as listas, containers para guardar vários conteúdos em Python

vetor = []
i = 1
while i <= 5:
    n = int(input("Digite um número: "))
    vetor.append(n)
    i += 1
print(f'Vetor lido: {vetor}')

# Faça um programa que leia um vetor de 10 números e mostre-os na ordem inversa
vetor = []
for c in range(0, 10):      # range([start], stop[, step]
    n = int(input(f"Digite {c + 1}° número: "))
    vetor.append(n)
print(vetor)
for c in range(len(vetor) - 1, -1, -1):  # range([start], stop[, step]
    print(vetor[c], end='  ')
print()
i = 9
while i != -1:
    print(vetor[i], end='  ')
    i -= 1
