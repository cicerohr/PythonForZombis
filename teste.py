from tatu import Cliente
from tatu import Conta

joao = Cliente('João da Silva', '777-1234')
maria = Cliente('Maria da Silva', '555-4321')
cicero = Cliente('Cícero Henrique Rodrigues', '5555-3214')
print(f'Nome: {joao.nome}. Telefone: {joao.telefone}.')
print(f'Nome: {maria.nome}. Telefone: {maria.telefone}.')
conta1 = Conta([joao], 1, 1000)
conta2 = Conta([maria, joao], 2, 500)
conta1.resumo()
conta2.resumo()
