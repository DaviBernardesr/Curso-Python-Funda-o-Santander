"""
Curso de Python Fundação Santander
"""

#Entrada e Saída de dados

"""
A entrada de dados é feita por input(), e saída por print()

se for int ou float, utilizar antes do input o tipo da variável, se for string não precisa.
no print, se for utilizar mais cadeias dentro, utilizar o f-string, colocando f antes dos "" e usando a variável com chaves {} e nome dentro.

input  =  nome_variavel = tipo_dado(input("Text"))
print = print(f"Text {nome_variavel} Text")
"""

nome = input("Seu nome: \n")

idade = int(input("Digite sua idade:\n"))


print(f"Seu nome é: {nome} e você tem {idade} completos\n")


#Cálculadora de Dízimo
salario = float(input("Digite seu salário atual: \n"))
dizimo_porcent = int(input("Digite a % de Dízimo entregue: \n"))

while dizimo_porcent < 10:
    print(f"Sua porcentagem de dízimo declarado é de: {dizimo_porcent}, o mínimo é 10%, atualize-a!!!\n")
    dizimo_porcent = int(input("Digite a % nova de Dízimo entregue: \n"))

    if dizimo_porcent >= 10:
        exit()


valor_pago_dizimo = salario / dizimo_porcent
print(valor_pago_dizimo)



