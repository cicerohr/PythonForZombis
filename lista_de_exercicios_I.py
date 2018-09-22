# Lista de Exercícios I

# 1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números
print('-' * 30)
n1 = int(input('1° número: '))
n2 = int(input('2° número: '))
print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
print('-' * 30)

# 2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
metro = int(input('Digite um valor em metros: '))
print(f'{metro}m ==> {metro * 1000}mm')
print('-' * 30)

# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos.
dias = int(input('Dia(s): '))
total = (((dias * 24) * 60) * 60)
horas = int(input('Hora(s): '))
total += ((horas * 60) * 60)
minutos = int(input('Minuto(s): '))
total += (minutos * 60)
segundos = int(input('segundo(s): '))
total += segundos
print(f'O total de segundos é {total}.')
print('-' * 30)

# 4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input('Salário: '))
aumento = float(input('Aumento: [%] '))
print(f'O novo salário será de R$ {salario * (aumento/100) + salario:.2f}.')
print('-' * 30)

# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
# preço a pagar.
preco = float(input('Preço: '))
desconto = float(input('Desconto: [%]: '))
valor_desconto = (preco * desconto / 100)
print(f'Você tem R$ {valor_desconto:.2f} de desconto. O total a pagar é R$ {preco - desconto:.2f}.')
print('-' * 30)

# 6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
# esperada para a viagem.
distancia = float(input('Distância: [km] '))
velocidade = float(input('Velocidade: [km/h] '))
print(f'A viagem durará {distancia/velocidade}h.')
print('-' * 30)

# 7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
celsius = float(input('Temperatura: [°C] '))
print(f'{celsius:.1f}°C ==> {9 * (celsius/5) + 32:.1f}°F')
print('-' * 30)

# 8) Faça agora o contrário, de Fahrenheit para Celsius.
fahrenheit = float(input('Temperatura: [°F] '))
print(f'{fahrenheit:.1f}°F ==> {5 * ((fahrenheit - 32) / 9):.1f}°C')
print('-' * 30)

# 9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
quilometros = float(input('km: '))
dias = int(input('Dias: '))
print(f'Total à pagar por {quilometros}km rodado(s) em {dias} dia(s): R$ {(60 * dias) + (0.15 * quilometros):.2f}')
print('-' * 30)

# 10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
# total de dias.
cigarros = int(input('Quantidade de cigarros / dia: '))
anos = int(input('Quantidade de anos fumando: '))
total_cigarros = anos * 365 * cigarros
k = (1/6)/24
print(f'O fumante já perdeu {total_cigarros * k:.2f} dias.')
print('-' * 30)

# 11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
# a um milhão.
a = len(str(2 ** 1000000))
print(f'2 ** 1000000 tem {a} caracteres.')
print('-' * 30)
