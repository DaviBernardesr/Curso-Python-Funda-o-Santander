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


#Variável Global

nome = "Davi Bernardes"

saudacao("Davi")

def prof(profissao):
    cargo = input("Digite o cargo que exerce extra: ")
    print(f"Olá {nome}, sua profissão é {profissao}, \nCargo Extra: {cargo}")

prof("Radialista")

#Func com argumentos indeterminados
def soma_valores(*valores):
    soma = 0
    for i in valores:
        soma += i

    return soma

result = soma_valores(1, 50, 60, 22)
print(result)