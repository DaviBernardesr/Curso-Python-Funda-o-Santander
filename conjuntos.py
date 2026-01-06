"""
Curso de Python Fundação Santander
"""

#Conjuntos são estruturas que assume valores, variados, e não misturados.
#Pode ser númericos, letras, etc

#EX:
# nome_conjunto = {"elem1", "elem2", "elem3"} ou nome_conjunto = set([1,2,3,4,5])

#Tem operações com conjuntos:
# | (OU), & (Interseção), - (Diferença), ^ (Diferença Simétrica)

conjunto1 = {"Davi", "Bruno", "Rafael"}
conjunto2 = {1,2,3,4,5}
conjunto3 = {3,4,5,6,7}
conjunto4 = set([1,2,3,4,5])
conjunto5 = {10, 20, 60, 70}


print(conjunto1)
print(conjunto2)
print(conjunto4)
print(f"O conjunto 5 é: {conjunto5}")



#Operações
diferenca = conjunto2 & conjunto3
print("Valor de diferença:", diferenca)

uniao = conjunto2 | conjunto3
print("Valor de união:", uniao)

#Métodos

conjunto1.add("Maria Eduarda")
print("Conjunto 1 pos add:", conjunto1)

conjunto1.remove("Maria Eduarda")
print("Conjunto 1 pos remove:", conjunto1)

conjunto1.clear()
print(conjunto1)