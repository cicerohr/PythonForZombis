# Lista de Exercícios II
#
print('-' * 30)
# 1. Faça um Programa que peça os três lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
a = int(input('Digite o 1° segmento de reta: '))
b = int(input('Digite o 2° segmento de reta: '))
c = int(input('Digite o 3° segmento de reta: '))
if abs(b - c) < a < b + c:  # verifica se forma um triângulo |b - c| < a < b + c
    if a == b == c:
        print(f'Os lados {a}, {b} e {c} formam um triângulo equilátero.')
    elif a == b or a == c or b == c:
        print(f'Os lados {a}, {b} e {c} formam um triângulo isósceles.')
    else:
        print(f'Os lados {a}, {b} e {c} formam um triângulo escaleno.')
else:
    print(f'Os lados {a}, {b} e {c} não formam um triângulo.')
print('-' * 30)

# 2. Determine se um ano é bissexto. Verifique no Google como fazer isso...
while True:
    continuar = ' '
    ano = int(input('Digite um ano: '))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} não é bissexto.')
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 30)

# 3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
# regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
# Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário mostrar tais variáveis com o conteúdo ZERO.
peso = float(input('Peso: [kg] '))
excesso = multa = 0
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
print(f'Você tem {excesso:.2f}kg de excesso e R$ {multa:.2f} de multa.')
print('-' * 30)

# 4. Faça um Programa que leia três números e mostre o maior deles.
while True:
    maior = 0
    continuar = ' '
    for c in range(1, 4):   # range([start], stop[, step]
        numero = int(input(f'Digite o {c}° número: '))
        if c == 1:
            maior = numero
        else:
            if numero > maior:
                maior = numero
    print(f'O maior número é {maior}.')
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 30)

# 5. Faça um Programa que leia três números e mostre o maior e o menor deles.
while True:
    maior = menor = 0
    continuar = ' '
    for c in range(1, 4):   # range([start], stop[, step]
        numero = int(input(f'Digite o {c}° número: '))
        if c == 1:
            maior = menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
    print(f'O número maior é {maior} e o menor é {menor}.')
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 30)

# 6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê o salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido.
# Observe que Salário Bruto - Descontos = Salário Líquido.
# Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato (5%) : R$
# e. = Salário Liquido : R$
valor_hora = float(input('Valor por hora: R$ '))
horas = int(input('Quantas horas? '))
salario_bruto = valor_hora * horas
ir = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - ir - inss - sindicato
print(f'\ta. + Salário Bruto: R$ {salario_bruto:4.2f}')
print(f'\tb. - IR (11%): R$ {ir:4.2f}')
print(f'\tc. - INSS (8%): R$ {inss:4.2f}')
print(f'\td. - Sindicato (5%): R$ {sindicato:4.2f}')
print(f'\te. = Salário Liquido: R$ {salario_liquido:4.2f}')
print('-' * 30)

# 7. Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
# que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
# Obs. : somente são vendidos um número inteiro de latas.
area = int(input('Qual é a área a ser pintada? [m²] '))
latas = round(area / 54)   # 1 lata ==> 54m²
print(f'É necessário {latas} lata(s) (18 litros) de tinta para pintar {area}m². \nPreço a pagar R$ {latas * 80:.2f}.')
print('-' * 30)
