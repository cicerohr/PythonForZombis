# 4.1 - TWP315 Arquivos
# Aprenda como ler e escrever seus dados em arquivos para serem levados a qualquer lugar :)

arquivo = open('numeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()
