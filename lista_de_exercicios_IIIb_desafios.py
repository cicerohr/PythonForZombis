# Lista de Exercícios IIIb – Desafios!
#
print('-' * 30)
# 1. Dizemos que um número natural é triangular se ele é produto de três números naturais
# consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120.
# Dado um inteiro não-negativo n, verificar se n é triangular.
n = int(input('Digite um número: '))
k = 0
while k * (k + 1) * (k + 2) < n:
    k += 1
print(k * (k + 1) * (k + 2) == n)
print('-' * 30)

# 2. Indique como um troco deve ser dado utilizando-se um número mínimo de notas.
# Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando os centavos.
# Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.
cedulas = [50, 20, 10, 5, 2, 1]
n_notas = {}
conta = float(input('Valor a ser pago: [R$] '))
pagamento = float(input('Pagamento: [R$] '))
troco = pagamento - conta
temp = troco
i = 0
while True:
    cedula = f'R$ {str(cedulas[i])},00'
    n_notas[cedula] = int(temp // cedulas[i])
    resto = temp % cedulas[i]
    temp = resto
    i += 1
    if resto == 0:
        print(f'Valor a ser pago: R$ {conta:.2f}\nTroco para R$ {troco:.2f}: ')
        for k, v in n_notas.items():
            if v != 0:
                print(f'\t- {v} nota(s) de {k}')
        break
print(n_notas)
print('-' * 30)

# 3. Verifique se um inteiro positivo n é primo.
cont = 1
n_divisoes = 0
numero = int(input('Digite um número inteiro: '))
while cont <= numero:
    if numero % cont == 0:
        n_divisoes += 1
    cont += 1
if n_divisoes == 2:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')

# 4. Dado um número inteiro positivo, determine a sua decomposição em fatores primos
# calculando também a multiplicidade de cada fator.
n = int(input('Número: '))
for k in range(2, n):
    while n % k == 0:
        print(k)
        n = n / k
print('-' * 30)

# 5. Faça um programa que peça um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321
numero = str(input('Digite um número: ')).strip()
print(f'O número {numero} invertido é {numero[::-1]}.')
print('-' * 30)
