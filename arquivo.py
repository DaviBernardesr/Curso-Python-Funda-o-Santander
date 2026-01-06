"""
Curso de Python Fundação Santander
"""

#Pode-se manipular arquivos em python também, sempre abrir e fechar arquivos, com .open() e .close()
#Estrutura:
# nome_variavel = open('nome arquivo' , 'r (read) ou w (write)'
# nome_variavel.close() #Fechar

# witch serve para abrir e fechar sozinho automático arquivos
# with open("nome", "tipo") as arquivo:
#     variavel = arquivo.read()
#     print(variavel)

arquivo = open('arquivo.txt', 'w')

a = 10
b = 20
c = 50

media_result = (a + b + c) / 3

arquivo.write(f"{media_result}")
arquivo.close()


arquivo = open('arquivo.txt', 'r')

result = arquivo.read()
print(f"Resultado puxado do arquivo: {result}")

arquivo.close()

#uso do With (abre e fecha sozinho)
with open("arquivo.txt", "r") as arquivo:
    result2 = arquivo.read()
    print(f"Resultado puxado do arquivo usando with: {result2}")
