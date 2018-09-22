# 6.1 - TWP050 dinâmica, forte e múltipla
# Os conceitos sobre linguagens dinâmicas, tipo forte e atribuições múltiplas.

a = 'abacate'
a = 42
b = 13
print(f'a = {a}, b = {b}')
a, b = b, a
print('a, b = b, a')
print(f'a = {a}, b = {b}')
a, b, c = 'OBA'
print('a, b, c = "OBA"')
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')