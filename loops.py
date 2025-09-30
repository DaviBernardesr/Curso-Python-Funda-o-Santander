"""
Curso de Python Santander
"""

#Loops são compostos por For(Para) ou While(Enquanto)
#for é feito para executar até o fim de uma sequência determinada na sua definição
#While executa enquanto uma condição for verdadeira

#For:
# for variavel in sequência:
#   bloco de código

#range determina a quantidade de iterações.
#break força a sair do loop no momento atual que ele é encontrado, saída do loop
#continue termina a instrução atual e passa p/ próxima dentro do loop
#pass serve apenas para marcação, não executa nada

for i in range (1,10):
    print(i)
    print('Testando o for utilizando range 1.0')

for j in range (0, 10):
    print(j)

#Vetor
nomes = ['Davi', 'Pedro', 'Thiago']

for i in range (0, 3):
    print(nomes[i])

for nomes in nomes:
    print(nomes)



#While:
#while condição:
#   bloco de código

#Criar um contador ou outra abordagem para o loop saber quando parar.

contador = 0

while contador < 5:
    print(contador)
    print("Contador sendo passado como condição de parada")
    contador += 1

#numeros vai imprimir somente os números impares.
numeros = [1,2,3,4,6,7,8,9]

for numeros in range (10):
    if numeros % 2 == 0:
        continue
    print(numeros)

#numeros vai imprimir somente os números pares.
numeros = [2,3,6,8,3,30,50]

for numeros in range (8):
    if numeros % 2 != 0:
        continue
    print(numeros)