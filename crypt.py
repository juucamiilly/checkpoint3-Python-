import base64
from Crypto.Cipher import AES


def main_crypt(key, file_path):

    global save_last_key_multiplo, save_last_multiplo
    aes = AES.new(key, AES.MODE_ECB)

    with open(file_path, "rb") as arquivo:
        binario = arquivo.read()
    arquivo.close()
    dado64 = base64.b64encode(binario)
    texto_limpo = dado64.decode('utf-8')
    texto_limpo = texto_limpo  # texto tem que ser multiplo da senha
    comprimento = len(texto_limpo) + 100

    if len(texto_limpo) % len(key) == 0:
        cripitado = aes.encrypt(texto_limpo)

        with open(file_path, 'wb') as cryptFile:
            cryptFile.write(cripitado)

    else:
        salvar = 1
        for x in range(1, comprimento):
                if len(texto_limpo) % x == 0:
                    old = salvar
                    salvar = x

                    if salvar > old:
                        save_last_multiplo = salvar

        sair = "entrar"
        for x in range(1, comprimento):
                if x < len(key):
                    if len(key) % x == 0:
                        if save_last_multiplo < x:
                            x = x
                else:
                    if x % len(key) == 0:
                        if sair != "sair":
                            if save_last_multiplo < x:
                                save_last_key_multiplo = x
                                sair = "sair"

        falta = save_last_key_multiplo - save_last_multiplo

        for x in range(1, (falta + 1)):
            texto_limpo = texto_limpo + "1"

        cripitado = aes.encrypt(texto_limpo)
        falta = ";" + str(falta)
        falta = falta.encode('ascii')

        with open(file_path, 'wb') as cryptFile:
            cryptFile.write(cripitado + falta)
        cryptFile.close()


