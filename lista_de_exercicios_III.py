# Lista de Exercícios III
#


def Fibonacci(n):
    """
    Usa recursividade para achar o número da sequência de Fibonacci de acordo com o índice passado como parâmetro
    :param n:
    :return Fibonacci(n - 1) + Fibonacci(n - 2):
    """
    if n <= 1:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print('-' * 30)
# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
    nota = float(input('Digite uma nota de 0 a 10: '))
    if 0 <= nota <= 10:
        print('Obrigado!')
        break
    else:
        print('Digite um número entre 0 e 10. Tente novamente!')
print('-' * 30)

# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    nome = str(input('Nome: ')).strip().upper()
    senha = str(input('Senha: ')).strip().upper()
    if senha == nome:
        print('Erro. A senha deve ser diferente do nome.')
    else:
        print('Obrigado!')
        break
print('-' * 30)

# 3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
# anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
# crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
# necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.
a = 8000
b = 20000
c = 0
while a <= b:
    a += (a * 3 / 100)
    b += (b * 1.5 / 100)
    c += 1
print(f'É necessário {c} anos para a população "A" ser maior igual a população "B".')
print('-' * 30)

# 4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
# formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores.
# Faça um algoritmo que leia um número inteiro calcule o seu número
# de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
# 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13
#     f1 + f2 = f3
numero = int(input('Digite um número: '))
f1 = f2 = 1
f3 = 0
print('1 -> 1 -> ', end='')
while f3 < numero:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f'{f3} -> ', end='')
print('Fim')
help(Fibonacci)
print('Fibonacci = ' + str(Fibonacci(10)))
print('-' * 30)

# 5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
# o algoritmo de Euclides.
a = a1 = int(input('a: '))
b = b1 = int(input('b: '))
while b != 0:
    r = a % b
    a = b
    b = r
print(f'O MDC dos inteiros {a1} e {b1} é {a}.')
print('-' * 30)
