# STRUCT PARA MANIPULAÇÃO DE ARQUIVOS

# open('arquivo', 'modo')
# 'arquivo' - nome do arquivo
# 'modo' - modo de abertura do arquivo


# MODOS DE INTERAGIR COM ARQUIVOS

# r - leitura de arquivo
# w - escrita de arquivo
# a - acrescentar ao arquivo / encrementar
# x - criação de arquivo
# + - atualização de arquivo
# r+ - leitura e escrita de arquivo


# EXEMPLO DE MANIPULAÇÃO DE ARQUIVOS

# arq = open("main/dados.txt", "r")
# print(arq.readable())
# print(arq.read())
# print(arq.readline())

# arq = open("main/banco_de_dados/dados.txt", "a")
# arq.write("Meg")

# arq = open("main/dados.txt", "r")
# lista = (arq.readlines())
# print(lista)
# print(lista[3])

# arq = open("main/banco_de_dados/dados.txt", "a")
# lista = ("Carro\n", "Moto\n", "Bicicleta\n")
# arq.writelines(lista)

# arq = open("main/banco_de_dados/dados3.txt", "w")
# arq.write("Carro\n")

# arq.close()


# REMOVENDO ARQUIVOS

# import os
# os.remove("main/banco_de_dados/dados3.txt")
# print("Arquivo removido com sucesso!")
