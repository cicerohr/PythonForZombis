# 4.1 - TWP325 Pseudo Cripto
# Aprenda como ler e escrever seus dados em arquivos para serem levados a qualquer lugar :)

texto = open('mensagem.txt')
saida = open('cripto.txt', 'w')
for linha in texto.readlines():
    for letra in texto.readlines():
        if letra in 'aeiou':
            saida.write('*')
        else:
            saida.write(letra)
texto.close()
saida.close()
