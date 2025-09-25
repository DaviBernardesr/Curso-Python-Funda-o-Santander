"""
Curso de Python Fundação Santander
"""

#Controla o fluxo dos programas
#Condicionais e Loop's

#IF
#if(condição):
#   trecho de código

idade = 23
if(idade >= 22):
    print("Você é mais velho!")


#IF-ELSE
#if(condição):
#   trecho de código
#else:
#   trecho de código

valor = 30
if(valor > 50):
    print("Você tem 1 dia de salário mínimo!")
else:
    print("Você ganha pouco demais!")


#IF-ELIF-ELSE
#if(condição):
#   trecho de código
#elif(condição):
#   trecho de código
#else:
#   trecho de código

saldo = 50.50
if(saldo > 50 and idade > 22):
    print("Você está com o dia ganho")
elif(saldo < 50 and idade > 22):
    print("Você está atrasado na vida")
else:
    print("Você não tem nada!")


nota = 25
if(nota > 15):
    print("Parabéns boa nota na prova")
else:
    print("Precissa melhorar!")

soma = nota + 30
soma = soma + 30

if(soma == 30):
    print("valor baixo!")
elif(soma <= 30):
    print("valor abaixo demais, melhore!")
elif(soma > 30):
    print("Parabéns, você conseguiu!!")
else:
    print("Você ficou de fora!")
