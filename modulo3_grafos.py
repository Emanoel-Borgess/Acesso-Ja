from collections import deque
import heapq


class Grafo:
    def __init__(self):
        self.vertices = []
        self.listaAdj = {}
        self.matrizAdj = []
        self.grausEntrada = {}

    def adicionarVertice(self, nomeVertice):
        if nomeVertice in self.vertices:
            return
        
        self.vertices.append(nomeVertice)
        
        self.listaAdj[nomeVertice] = []
        self.grausEntrada[nomeVertice] = 0
        
        for linha in self.matrizAdj:
            linha.append(0)

        novaLinha = [0] * len(self.vertices)
        self.matrizAdj.append(novaLinha)
    
    def adicionarAresta(self, origem, destino, custo):
        if origem not in self.vertices or destino not in self.vertices:
            print("Erro: Um dos vértices não existe.")
            return

        self.listaAdj[origem].append((destino, custo))
        
        self.listaAdj[destino].append((origem, custo))

        i_origem = self.vertices.index(origem)
        i_destino = self.vertices.index(destino)

        self.matrizAdj[i_origem][i_destino] = custo
        
        self.matrizAdj[i_destino][i_origem] = custo

    def adicionarDependencia(self, tarefaAntes, tarefaDepois):
        if tarefaAntes not in self.vertices or tarefaDepois not in self.vertices:
            return
        
        self.listaAdj[tarefaAntes].append((tarefaDepois, 0))
        
        self.grausEntrada[tarefaDepois] += 1
    
    def imprimirListaAdj(self):
        print("\n--- Lista de Adjacências (Vizinhos) ---")
        for vertice in self.listaAdj:
            print(f"{vertice} -> {self.listaAdj[vertice]}")

    def imprimirMatrizAdj(self):
        print("\n--- Matriz de Adjacências (Tabela) ---")
        
        print("      ", end="")
        for vertice in self.vertices:
            print(f"{vertice[:5]:7}", end="") 
        print()

        for i, linha in enumerate(self.matrizAdj):
            nome_vertice = self.vertices[i]
            print(f"{nome_vertice[:5]:5} |", end="")
            
            for valor in linha:
                print(f"{valor:6}", end=" ")
            print("|")

    def buscaDFS(self, origem):
        visitados = set()
        self.dfsRecursivo(origem, visitados)

    def dfsRecursivo(self, verticeAtual, visitados):
        visitados.add(verticeAtual)
        print(verticeAtual, end=" -> ")

        for vizinho, custo in self.listaAdj[verticeAtual]:
            if vizinho not in visitados:
                self.dfsRecursivo(vizinho, visitados)


    def buscaBFS(self, origem):
        visitados = set()
        fila = deque([origem])
        visitados.add(origem)

        print(f"\nIniciando BFS a partir de '{origem}':")

        while fila:
            verticeAtual = fila.popleft()
            print(verticeAtual, end=" -> ")

            for vizinho, custo in self.listaAdj[verticeAtual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

    def dijkstra(self, origem, destinoFinal):
        distancias = {v: float('inf') for v in self.vertices}
        distancias[origem] = 0
        anteriores = {v: None for v in self.vertices}
        pq = [(0, origem)]

        while pq:
            distanciaAtual, verticeAtual = heapq.heappop(pq)
            if verticeAtual == destinoFinal:
                break

            if distanciaAtual > distancias[verticeAtual]:
                continue

            for vizinho, pesoAresta in self.listaAdj[verticeAtual]:
                novaDistancia = distanciaAtual + pesoAresta
                if novaDistancia < distancias[vizinho]:
                    distancias[vizinho] = novaDistancia
                    anteriores[vizinho] = verticeAtual
                    heapq.heappush(pq, (novaDistancia, vizinho))

        caminho = []
        passoAtual = destinoFinal
        
        if distancias[destinoFinal] == float('inf'):
            print(f"Não há caminho entre {origem} e {destinoFinal}.")
            return [], float('inf')

        while passoAtual is not None:
            caminho.insert(0, passoAtual)
            passoAtual = anteriores[passoAtual]

        return caminho, distancias[destinoFinal]

    # MST - Algoritmo de Borůvka
    def boruvkaMST(self):
        parent = {v: v for v in self.vertices}
        rank = {v: 0 for v in self.vertices}

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                return True
            return False

        mst_arestas = []
        custo_total = 0
        
        todas_arestas = []
        arestas_vistas = set()
        for u in self.listaAdj:
            for v, peso in self.listaAdj[u]:
                edge_id = tuple(sorted((u, v)))
                if edge_id not in arestas_vistas:
                    todas_arestas.append([u, v, peso])
                    arestas_vistas.add(edge_id)

        num_arvores = len(self.vertices)

        while num_arvores > 1:
            menor_aresta = {}
            for u, v, w in todas_arestas:
                set1 = find(u)
                set2 = find(v)
                if set1 != set2:
                    if set1 not in menor_aresta or w < menor_aresta[set1][2]:
                        menor_aresta[set1] = [u, v, w]
                    if set2 not in menor_aresta or w < menor_aresta[set2][2]:
                        menor_aresta[set2] = [u, v, w]

            arestas_adicionadas = 0
            for raiz in menor_aresta:
                u, v, w = menor_aresta[raiz]
                set1 = find(u)
                set2 = find(v)
                if set1 != set2:
                    union(u, v)
                    mst_arestas.append((u, v, w))
                    custo_total += w
                    num_arvores -= 1
                    arestas_adicionadas += 1
            
            if arestas_adicionadas == 0:
                break

        return mst_arestas, custo_total

    # 2. Coloração - Welch-Powell
    def coloracaoWelchPowell(self):
        verticesOrdenados = sorted(self.vertices, key=lambda v: len(self.listaAdj[v]), reverse=True)
        coresAtribuidas = {}
        corAtual = 0

        while len(coresAtribuidas) < len(self.vertices):
            corAtual += 1
            for vertice in verticesOrdenados:
                if vertice not in coresAtribuidas:
                    podePintar = True
                    for vizinho, peso in self.listaAdj[vertice]:
                        if vizinho in coresAtribuidas and coresAtribuidas[vizinho] == corAtual:
                            podePintar = False
                            break
                    if podePintar:
                        coresAtribuidas[vertice] = corAtual
        return coresAtribuidas

    def ordenacaoTopologica(self):
        graus = self.grausEntrada.copy()
        fila = deque([v for v in self.vertices if graus[v] == 0])
        ordemTopologica = []

        while fila:
            atual = fila.popleft()
            ordemTopologica.append(atual)
            for vizinho, peso in self.listaAdj[atual]:
                graus[vizinho] -= 1
                if graus[vizinho] == 0:
                    fila.append(vizinho)

        if len(ordemTopologica) != len(self.vertices):
            return ["Erro: Ciclo detectado!"]
        return ordemTopologica