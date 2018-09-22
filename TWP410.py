# 9.1 - TWP410 Python em baixo nível módulo dis
# Como criar e consultar banco de dados em Python e vendo python por baixo dos panos :)

import dis


def f(n):
    k = 1
    f = 1
    while k <= n:
        f = f * k
        k = k + 1
    return f


dis.dis('c = a + b')
print('-' * 50)
dis.dis(f)
