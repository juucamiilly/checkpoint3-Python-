#!/usr/bin/env python

from crypt import main_crypt
from decrypt import main_decrypt


def main():
    print("Selecione uma opcao:")
    print(' 1) Encripitografar arquivo')
    print(' 2) Descripitografar arquivo')
    print(' 3) Sair\n\n')
    resp = int(input(">"))

    if resp == 1:
        print("\nInsira o caminho pro arquivo:\n")
        file = input(">")

        print("\nInsira a chave de criptografia:\n")
        key = input(">")

        main_crypt(key, file)
        print("\nSeu arquivo foi encriptado com sucesso.\n")

    elif resp == 2:
        print("\nInsira o caminho pro arquivo:\n")
        file = input(">")

        print("\nInsira a chave de criptografia:\n")
        key = input(">")

        main_decrypt(key, file)
        print("\nSeu arquivo foi descriptado com sucesso.\n")

    elif resp == 3:
        exit()
    else:
        main()


main()



