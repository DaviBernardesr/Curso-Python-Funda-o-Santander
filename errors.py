"""
Curso de Python Fundação Santander
"""

#O Python oferece o tratamento de exceção, onde não se para todo o código, e sim a parte que está com erro.

#Existe tipos de erros:
"""
TypeError: erro de tipo, atribuindo um valor a uma váriavel ou algo que não condiz
SyntaxError: erro de sintaxe do código, escrito fora da forma padrão de lógica do python
NameError: erro de nome em uma chamada ou variável, tenta acessar algo errado (nome inexistente)
IndexError: erro do index, tenta acessar um indice errado não existente etc.
"""

#Para lidar com essas exceções, utiliza-se trechos para fazer o manejo e lidar de forma mais direta>

"""
Try:
    trecho de código
    
except nome_exceção:
    trecho de código
    
finally: (ocorre sempre que definir, fechando ou disparando comando).
    trecho de código
"""


try:
    valor = int(input("Digite seu saldo: \n"))
    if valor % 2 == 0:
        print("Saldo Par!")
        print(f"\nValor: {valor}")
except ZeroDivisionError:
    print("Saldo Negativo, error")
finally:
    print("Programa Finalizado")

