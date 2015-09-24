# N quantidade de numeros que tem na lista
N = 20
# exposicao dos numero da lista
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
# imprimir a lista no formato original 
print("lista original", lista)
# criamos um grafico
import matplotlib.pyplot as plt
x = range(0,N,1)
#criamos a figura do grafico
plt.figure()
# plotamos x por y
plt.plot(x,lista,'ok')
# para por o titulo na grafico e nos eixos
plt.title("grafico inicial")
plt.xlabel("x eh posicao")
plt.ylabel("y eh valor")
# salvar a figura na pasta fig
plt.savefig("fig/bubble-inicio.png")
# fechar a figura
plt.close()
mudanca = 1
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
            plt.figure()
            plt.plot(x,lista,'ok')
            plt.title("grafico inicial")
            plt.xlabel("x eh posicao")
            plt.ylabel("y eh valor")
            plt.savefig("fig/bubble-troca-{}.png".format(mudanca))
            plt.close()
            mudanca = mudanca + 1
# imprimir a lista original em ordem crescente			
print("lista crescente", lista)
print("lista dos cinco menores", lista[0:5])
print("lista dos cinco maiores", lista[N-5:N])
x = range(0,N,1)
plt.figure()
plt.plot(x,lista,'ok')
plt.title("grafico inicial")
plt.xlabel("x eh posicao")
plt.ylabel("y eh valor")
plt.savefig("fig/bubble-fim.png")
plt.close()


