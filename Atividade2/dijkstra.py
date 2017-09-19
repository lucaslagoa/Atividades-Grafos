from  igraph import *

#gera um grafo automaticamente
G = Graph.Erdos_Renyi(n=5, m=5)
G.vs["label"] = ["0","1","2","3","4"]

#adj = G.get_adjacency()
#print(adj)

matriz_distancias = [[0 for x in range(5)] for y in range(5)] 
#print (matriz_distancias)

for x in range(0, 5):
	for y in range(0, 5):
		matriz_distancias[x][y] = G.shortest_paths_dijkstra(G.vs.select(x),G.vs.select(y))
		#print(matriz_distancias[x][y])

print("\n")
maior = 0
menor = 10
ex = [0 for x in range(5)]
for x in range(0, 5):
	for y in range(0, 5):
		if(menor > matriz_distancias[x][y] or (x == 0 and y == 0)):
			menor = matriz_distancias[x][y]
		if(maior < matriz_distancias[x][y]):
			maior = matriz_distancias[x][y]
		if(ex[x] < matriz_distancias[x][y]):
			ex[x] = matriz_distancias[x][y]

	print "A excentricidade do vertice ", x, "eh: ", ex[x]

print "O diametro e:" , maior
print "O raio e:" , menor

for x in range(0, 5):
	if(ex[x] == maior):
		print x, " e periferia"

plot(G, layout="fr")
#funcao katyadjkstra
