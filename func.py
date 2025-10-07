"""
Curso de Python Fundação Santander
"""

#Funções (trechos de códigos reutilizáveis para melhorar identação e legibilidade
#Código:
#def nome_funcao ():      #() Argumentos
#   trecho de código

#Variáveis declaradas fora são global
#return devolve valor da função

def saudacao(nome):
    idade = input("Digite sua idade: ")
    print(f"\nOlá seja bem-vindo, {nome} Sua idade é: {idade}")


saudacao("Davi")

