"""
Curso de Python Fundação Santander
"""

#Dicionários é uma estrutura de dados editavel e não ordenada, armazena valores de acordo com chave-valor recebido, e tem métodos para manusear.
#EX:
# variavel = {"atributo1": "valor1", "atributo2": "valor2", etc}

#Para acessar, basta refêrenciar o nome da variavel e indicar a chave de acesso.
#EX:
# print(variavel["chave"]

#Tem métodos para controlar os dicionarios, como o keys(), mostra as chaves, values(), mostra o conteúdo, items(), mostra chaves e valores juntos
#e tem o update(novo item), que adiciona nova chave e valor.

dicionario1 = {"nome": "Davi", "idade": "22", "Trabalho": "Desenvolvedor"}

print(dicionario1["idade"])
print(dicionario1["nome"])

print(dicionario1.keys())
print(dicionario1.values())
print(dicionario1.items())

#Alterando:

dicionario1.update({"Curso": "Sistemas de Informação"})
print(dicionario1.values())