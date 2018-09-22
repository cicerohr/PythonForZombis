# 1.1 - TWP274 Média de quatro notas
# Faça um programa que leia um vetor de 10 caracteres minúsculos e diga quantas consoantes foram lidas.

vogais = 'aeiou'
vetor = ''
espaco = -1
while len(vetor) != 10 or espaco != -1:  # Verifica se tem 10 caracteres e não tem espaços
    vetor = str(input('Digite 10 letras sem acento: ')).strip().lower()
    espaco = vetor.find(' ')
    if len(vetor) != 10:
        print(f'Você digitou {len(vetor)} caracteres.')
    elif espaco != -1:
        print(f'O {espaco + 1}° caracter é um espaço.')
    else:
        break
for i in range(0, len(vogais)):  # Retiras as vogais
    vetor = vetor.replace(vogais[i], '')
    print(f'{vetor} procurou a vogal {vogais[i]}.')
print(f'Há {len(vetor)} consoante(s).')
