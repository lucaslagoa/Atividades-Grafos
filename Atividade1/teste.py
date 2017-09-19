from  igraph import *

G = Graph.GRG(10,0.2)  #eh gerado automaticamente um grafo com 10 vertices 

print(G.as_directed().indegree())  #imprime a lista com o numero de arestas que saem de cada vertice
print(G.as_directed().outdegree()) #imprime a lista com o numero de arestas que entram em cada vertice

listaOutDegree = G.as_directed().outdegree() 
listaInDegree = G.as_directed().indegree()

for x in range(0,10):  #eh realizada a intersessao entre os vertices que saem e entram, e se o valor for maior que zero em ambos, eh um componente fortemente conectado
	if listaInDegree[x] > 0 and listaOutDegree[x] > 0:
		print("Componente fortemente conectado",x)


#print(G.as_directed().components(mode=STRONG))
plot(G.as_directed())