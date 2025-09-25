
"""
Variáveis e Identenção Python
"""

#Não tem que declarar o tipo, somente criar e atribuir valor ou caracter.
#Não tem {} no meio da identação, somente usar espaço e tabulação dentro da func, if/else, repetição etc.
#Não utilizar ; no final, somente se for mais de uma atribuição em uma mesma linha.

#Sempre utilizar o ínicio da linha na esquerda.

nome = "Bruno"
letra = 'a'

idade = 22
peso = 11.5

aprovado = True
reprovado = False

#Tipos de dados, int, float, string, booleano, não precisa atribuir.
#if e else utiliza if/else() na estrutura:

print("Ficha Pessoal do Curso:\n")
print (nome)
print (idade)
print (peso)

if(nome == "Davi"):
    print(idade)
    print(peso)
else:
    print("Você não é o Davi\n")

if(aprovado == True):
    print("Davi foi aprovado\n")
else:
    aprovado = False
    print("Você foi reprovado\n")


if(peso > 20):
    print("Você está bem!\n")
else:
    print("Você está mal, procure ajuda!\n")

if(nome == "Davi" and aprovado == True):
    print("Parabéns, você cumpriu seu objetivo")
else:
    print("Você não cumpriu seu objetivo")