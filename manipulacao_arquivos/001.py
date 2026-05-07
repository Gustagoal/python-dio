# with open("teste.txt","w") as arquivo:
#     arquivo.write("Reforçando manipulação de arquivos")

# with open("teste.txt","r") as arquivo:
#     leitura = arquivo.read()

# print(leitura)

with open("teste.txt","a") as arquivo:
    arquivo.write("Novo registro")


with open("teste.txt","r") as arquivo:
        for linha in arquivo:
              print(linha.split())