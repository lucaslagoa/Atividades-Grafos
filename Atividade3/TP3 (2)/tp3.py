from igraph import * 
import numpy as np 
def find_all_paths2(G, start, end, vn = []): #algoritmo achaado na internet que retorna todos os caminhos
	vn = vn if type(vn) is list else [vn]
	#vn = list(set(vn)-set([start,end]))
	path  = []
	paths = []
	queue = [(start, end, path)]
	while queue:
	    start, end, path = queue.pop()
	    path = path + [start]

	    if start not in vn:
	        for node in set(G.neighbors(start,mode='OUT')).difference(path):
	            queue.append((node, end, path))

	        if start == end and len(path) > 0:              
	            paths.append(path)
	        else:
	            pass
	    else:
	        pass
	return paths
def ford_fulkerson(matriz, lista, tamanho): #seleciona os caminhos 
	tamanho_lista = len(lista)
	fluxo=[0 for i in range (tamanho_lista)]
	for i in range(tamanho_lista):
		tamanho_lista_2 = len(lista[i])
		for j in range(tamanho_lista_2):
			if(j==0):
				posicao = lista[i][0]
				for k in range (tamanho):
					if(matriz[posicao][k]!=0):
						fluxo[i]= matriz[posicao][k]
						break
			posicao = lista[i][j]
			for k in range (tamanho):
				aux = matriz[posicao][k]
				if((fluxo[i]>aux)and(aux!=0)):
					fluxo[i]=aux
	return fluxo
def matriz_adjacencia(G, tamanho):#implementa matriz de adjacencia do grafo
	matriz = np.zeros(shape = (tamanho, tamanho))
	k=0
	for i in range (tamanho):
		l=0
		for j in range (tamanho):
			if(j==0):
				num_vizinhos = G.neighborhood_size(i, mode = OUT)
				vertices_adjacentes = np.zeros(shape = (num_vizinhos))
				vertices_adjacentes = G.neighbors(i, OUT)
			if(l!=num_vizinhos-1):
				posicao = vertices_adjacentes[l]
				matriz[i][posicao] = G.es[k]['weight'];
				k=k+1;
				l=l+1
	return matriz
G = Graph()
G = Graph.Read_Ncol("entrada2.txt", directed = True)	
tamanho = G.vcount()
start = 0 
end = 5
lista = find_all_paths2(G, start, end, vn = [])
matriz = matriz_adjacencia(G, tamanho)
fluxo = ford_fulkerson(matriz, lista, tamanho)
fluxo.sort(reverse=True)
print fluxo
print fluxo[0]