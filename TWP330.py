# 4.1 - TWP330 Validação Endereço IP
# Aprenda como ler e escrever seus dados em arquivos para serem levados a qualquer lugar :)


def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True


arq = open('IPS.txt')
validos = open('validos.txt', 'w')
invalidos = open('invalidos.txt', 'w')
for linha in arq.readlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)
arq.close()
validos.close()
invalidos.close()
