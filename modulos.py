"""
Curso de Python Fundação Santander
"""

#Em python usa módulos (func prontas) prontos para poder ter mais rapidez ao manusear programas.

#Usa o comando import,
#import (nome_modulo) ou from (nome_modulo) import (func_exata)

# se importar somente o módulo, precisa sempre que for acessar a func, usar o comando nome_modulo.func e se usar o import mais específico,
# não precisa passar o nome somente a func direto.

import math

a = 10

#Calcular a raiz quadrada de 10.
result = math.sqrt(a)
print(result)

from math import pi

#Imprime o valor de pi.
result2 = pi
print(result2)

import random

#gera um número aleátorio.
num = random.randint(1, 200)
print(f"O número é: {num}")

import datetime

#Importa a data e hora atual.
data = datetime.datetime.now()
print(data)

hora = data.strftime("%H:%M:%S")
print(f"Hora exata: {hora}")

a = 10
b = 20

import somar

#Usando módulo própio
num = somar.somar(a, b)
print(num)

#Usando módulo própio
vrt = somar.multply(a, 10)
print(vrt)

