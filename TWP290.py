# 1.1 - TWP290 For é um While Enrustido
# Aprenda a como varrer as sequências de elementos com o comando for.

# Comando for.
print(f' Código com for '.center(30, '='))
for letra in 'aeiou':
    print(letra)
print('-' * 20)
for i in range(5):
    print(i)
print('-' * 20)
for x in ['cpbr6', 42, 3.14]:
    print(x)

# Comando while.
print(f' Código com while '.center(30, '='))
texto = 'aeiou'
k = 0
while k < len(texto):
    letra = texto[k]
    print(letra)
    k += 1
print('-' * 20)
lista = list(range(5))
k = 0
while k < len(lista):
    i = lista[k]
    print(i)
    k += 1
print('-' * 20)
lista = ['cpbr6', 42, 3.14]
k = 0
while k < len(lista):
    x = lista[k]
    print(x)
    k += 1
