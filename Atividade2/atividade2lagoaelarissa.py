from  igraph import *

#gera um grafo automaticamente
G = Graph.Erdos_Renyi(n=10, m=15)
#numeracao dos vertices
G.vs["label"] = ["0","1","2","3","4","5","6","7","8","9"]
#tamanho para gerar a matriz de distancias
tam = 10
matriz_distancias = [[0 for x in range(tam)] for y in range(tam)] 

#estrutura de repeticao para a geracao da matriz de distancias atraves do algoritmo de dijkstra

for x in range(0, tam):
	for y in range(0, tam):
		matriz_distancias[x][y] = G.shortest_paths_dijkstra(G.vs.select(x),G.vs.select(y))

#declaracao de variaveis e vetores que serao utilizados posteriormente
maior = 0
raio = 1
zero = 0 
soma = 0
soma = [0 for x in range(tam)]
ex = [0 for x in range(tam)]

#estrutura de repeticao para comparar e gerar o diametro, raio e excentricidade
for x in range(0, tam):
	for y in range(0, tam):
		if(maior < matriz_distancias[x][y]):
			maior = matriz_distancias[x][y]
		if(ex[x] < matriz_distancias[x][y]):
			ex[x] = matriz_distancias[x][y]
		if(ex[x] > 0 and matriz_distancias[x][y] < raio):
			raio = matriz_distancias[x][y]
		
		soma[x] = matriz_distancias[x][y][0][0] + soma[x]

	print "A excentricidade do vertice ", x, "eh: ", ex[x]

#estrutura de repeticao para gerar o centro do grafo 
for x in range(0, tam):
	if (ex[x] == raio):
		print "O centro do grafo eh o vertice ", x

#estrutura de repeticao para gerar o centroide do grafo
aux = 100
centroide = 0
for x in range(0, tam):
	if (soma[x] < aux and soma[x] > 0):
		centroide = x
		aux = soma[x]

print "O centroide do grafo eh o vertice ", centroide
print "O diametro e:" , maior
print "O raio e:" , raio

#estrutura de repeticao para gerar as periferias do grafo
for x in range(0, tam):
	if(ex[x] == maior):
		print x, " e periferia"

plot(G, layout="fr")
