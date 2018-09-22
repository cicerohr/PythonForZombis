# 4.1 - TWP310 Arquivos
# Aprenda como ler e escrever seus dados em arquivos para serem levados a qualquer lugar :)

arquivo = open('numeros.txt', 'w')
for linha in range(1, 101):
    arquivo.write(f'{linha}\n')
arquivo.close()
