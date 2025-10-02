"""
Curso Python Fundação Santander
"""

#Tuplas em Python é uma "lista" sem ser modificada após criação, sequência de dados ordenados , utiliza () para abrir e fechar.
# nome_variavel = (elem1, elem2, elem3, elem4).

#tuplas não podem ser modificadas, são heterogêneas.

tupla1 = (1,2,5,6)

tupla2 = (3,6,8)

print(tupla1[2])

print(tupla2[2])

print(tupla1[3])

#As Tuplas tem métodos para contar quantas vezes aparece o número, indice da aparicição do elemento, count(elemento), index(elemento),
#len(tupla)

print(tupla1.count(2))
print(tupla2.index(3))
print(tupla1.index(5))
print(len(tupla1))