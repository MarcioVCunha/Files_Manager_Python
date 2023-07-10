import os

pasta = input("Qual pasta gostaria de organizar?")

while(not os.path.exists(pasta)):
    pasta = input("Esta pasta não existe, gostaria de organizar outra?")

os.chdir(pasta)

lista_arquivos = [arquivo.lower() for arquivo in os.listdir() if os.path.isfile(arquivo)]
set_tipos = {tipo.split(".")[-1] for tipo in lista_arquivos}

for tipo in set_tipos:
    if not os.path.exists(tipo):
        os.mkdir(tipo)

for arquivo in lista_arquivos:
    pasta_destino = arquivo.split(".")[-1]
    de = os.path.join(os.getcwd(), arquivo)
    para = os.path.join(os.getcwd(), pasta_destino, arquivo)
    if os.path.exists(de):
        os.replace(de, para)