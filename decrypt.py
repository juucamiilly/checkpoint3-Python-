import base64
from Crypto.Cipher import AES
import re


def main_decrypt(key, file_path):

    aes = AES.new(key, AES.MODE_ECB)

    with open(file_path, "rb") as arquivo:
        conteudo = arquivo.read()
    arquivo.close()

    if re.search(b';', conteudo):
        hash = conteudo.split(b';')[0]
        bits = conteudo.split(b';')[1].decode('ascii')

        descriptado = aes.decrypt(hash)
        decrypt = base64.b64encode(descriptado)
        texto_limpo = base64.b64decode(decrypt)
        texto_limpo = texto_limpo.decode('ascii')

        for x in range(1, (int(bits) + 1)):
            texto_limpo = texto_limpo[:-1]

        original = texto_limpo.encode('ascii')
        original = base64.b64decode(original)

        with open(file_path, 'wb') as file:
            file.write(original)

    else:
        descriptado = aes.decrypt(conteudo)
        original = base64.b64decode(descriptado)
        with open(file_path, 'wb') as file:
            file.write(original)
        file.close()
