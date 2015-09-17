# N quantidade de numeros que tem na lista
N = 20
# exposicao dos numero da lista
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
# de quanto em quanto sera organizado a lista
for i in range(0,N-1,1) :
# FOR IN RANGE e um comando que gera a lista 
    for j in range(i+1,N,1) :
# comando que realiza a troca dos elementos da lista toda vez que i for maior do que j
        if lista[i] > lista[j]:
# cria uma variavel que guarda os elementos da lista i, temporariamente, enquanto estao ocorrendo as trocas
            temp = lista[i]
# Depois disso podemos igualar a variavel i com o elemento da variavel j
            lista[i] = lista [j]
# em seguida, podemos associar o elemento da lista j a variavel temp, pois trocamos de lugar a variavel i e a variavel j
            lista[j] = temp 
print(lista)
