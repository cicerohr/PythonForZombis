# 9.1 - TWP405 Banco de Dados
# Como criar e consultar banco de dados em Python e vendo python por baixo dos panos :)

import sqlite3

banco = sqlite3.connect('surfersDB.sdb')
banco.row_factory = sqlite3.Row
cursor = banco.cursor()
cursor.execute('select * from surfers where age > 25')
linhas = cursor.fetchall()
print('-' * 35)
for linha in linhas:
    print(f'{"Nome: ".rjust(7)}{linha["name"]}')
    print(f'{"País: ".rjust(7)}{linha["country"]}')
    print(f'{"Idade: ".rjust(7)}{linha["average"]}')
    print(f'{"Média: ".rjust(7)}{linha["board"]}')
    print(f'{"Idade: ".rjust(7)}{linha["age"]}')
    print('-' * 35)
cursor.close()

# Cria um banco de dados. Deve rodar uma única vez.
#
# con = sqlite3.connect('aluno.bd')
# cur = con.cursor()
# cur.execute('create table alunos(login varchar(8), ra integer)')
#
# cur.close()
# con.close()


con = sqlite3.connect('aluno.bd')
cur = con.cursor()
cur.execute('insert into alunos values("masanori", 42)')
cur.execute('insert into alunos values("emengarda", 666)')
cur.execute('select * from alunos')
for x in cur.fetchall():
    print(x)
cur.close()
con.commit()
con.close()
