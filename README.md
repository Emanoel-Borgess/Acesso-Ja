# Projeto: “Acesso Já: O Roteirizador Urbano Acessível”
## Aluno: Emanoel R. Borges

# Fase 1 — Busca de Dados (Sequencial, Binária e Texto)
### Entrega: 04/11 e 11/11

Este módulo implementa algoritmos de Busca Sequencial, Busca Binária e Busca em Texto (Rabin-Karp), adaptados ao contexto do projeto “Acesso Já”, simulando desafios reais de acessibilidade urbana.

## Desafio 1 — Busca Sequencial (Registros Desorganizados)

- **Algoritmo:** `busca_sequencial()`
- **Cenário no Acesso Já:** Simula a busca por um "Ponto de Interesse" (POI) específico (ex: "POI_hospital_central") dentro de uma lista de registros.
- **Funcionamento:**  A função varre a lista, item por item (do índice 0 até o fim), contando cada comparação. Ela para assim que encontra o alvo ou chega ao fim da lista.

## Desafio 2 — Busca Binária (Catálogos Ordenados)

- **Algoritmo:** `busca_binaria()`
- **Cenário no Acesso Já:** Simula a busca por um CEP específico dentro de um catálogo de CEPs que veio devidamente ordenado. Isso é usado para verificar rapidamente a existência de um CEP em nossa base de dados.
- **Funcionamento:** A função usa a abordagem de "dividir para conquistar". Ela olha o meio da lista: se o alvo for maior, joga a metade esquerda fora; se for menor, joga a metade direita fora. Ela repete isso até encontrar o alvo ou o espaço de busca desaparecer.

## Desafio 3 — Busca em Texto (Rabin-Karp)
### Entrega: 11/11

- **Algoritmo:** `rabin_karp()`
- **Cenário no Acesso Já:** Simula o "Desafio 3: Decifrando os Relatos de Usuários". O algoritmo analisa um "Tomo Antigo" (um texto longo com relatos de usuários) para encontrar "Marcas de Corrupção" (palavras-chave de inacessibilidade como "escada", "buraco" e "degrau").
- **Funcionamento:** O algoritmo implementa um rolling hash (hash deslizante). Em vez de comparar letras, ele compara "números mágicos" (hashes) da janela de texto com o hash do padrão. Isso é muito rápido. Quando os hashes batem, ele faz uma verificação final letra por letra para evitar falsos positivos (colisões). No meu teste, ele identificou com sucesso todas as ocorrências das palavras-chave nos relatos.

# Análise de Complexidade
### O programa principal (main()) demonstra a diferença de eficiência:

### Busca Sequencial (pior caso): `O(n)`
- No teste, para encontrar o alvo na posição 75 de uma lista de 100 CEPs, foram necessárias 76 comparações. No pior caso, se o alvo fosse o último, seriam 100 comparações.

### Busca Binária (pior caso): `O(log n)`
- Para encontrar o mesmo alvo (posição 75), a Busca Binária precisou de apenas 6 comparações. Isso prova que ela é exponencialmente mais rápida para lidar com grandes volumes de dados ordenados.

### Rabin-Karp (caso médio): `O(n + m)`
- O algoritmo consegue analisar um texto de n caracteres para encontrar um padrão de m caracteres de forma muito eficiente (quase linear). É imensamente mais rápido do que uma busca por força bruta ($O(n*m)$).

---

# Fase 2 — Otimização de Recursos (Compressão de Huffman)
### Entrega: 17/11

Este módulo faz a implementação do algoritmo de **Compressão de Huffman**, usado para reduzir o tamanho dos relatos de usuários armazenados no sistema "AcessoJá".

## Desafio — Compressão e Descompressão Huffman
- **Algoritmos:** `comprimir()` e `descomprimir()` (usando a `class No`)

- **Cenário no Acesso Já:** Compactação eficiente dos "Relatos de Usuários" (do Módulo 1) para reduzir o espaço de armazenamento no servidor.
- **Funcionamento (comprimir):** Constrói a Árvore de Huffman a partir de uma Fila de Prioridade (`heapq`), gera um mapa de códigos binários (o "dicionário esperto") e "traduz" o texto original, retornando o texto comprimido e a árvore (a "chave").
- **Funcionamento (descomprimir):** Lê o texto comprimido bit a bit, "caminha" pela árvore (0=esquerda, 1=direita) e, ao encontrar uma folha (letra), salva o caractere e retorna ao topo da árvore, reconstruindo o texto original.

# Análise de Complexidade e Resultados (Huffman)

### Compressão de Huffman (pior caso): `O(n + k log k)`
- (Onde `n` é o tamanho do texto e `k` é o número de caracteres únicos). A eficiência vem de construir a árvore de frequência (o `heap`) de forma otimizada. Resultados da Demonstração:

- **Eficiência:** O texto original dos relatos foi comprimido de **2568 bits** para **1329 bits**.
  - **Redução: 48,25%**
- **Integridade:** O texto restaurado pela função `descomprimir` foi verificado contra o original.
  - **Textos são idênticos? `True`**

---

# Fase 3 — Grafos ( O mapa do meu mundo)
### Entrega: 24/11

Nesta fase, iniciei a implementação da estrutura de dados central do projeto "Acesso Já": o **Grafo**. Ele representa o mapa da cidade, onde os locais são vértices e as rotas são arestas com peso.

## Desafio — Fundamentos do mundo, representação e conceitos básicos

- **Estrutura:** Classe `Grafo` (implementando Matriz e Lista simultaneamente).
- **Cenário no Acesso Já:** Mapeamento de cruzamentos e locais (Vértices) e calçadas/ruas (Arestas). O "peso" das arestas representa o **Custo de Acessibilidade** (ex: piso plano = 1, buracos = 10, ladeira = 5).

### Implementação e Funcionalidades

1.  **Representação Dupla:**
    * **Matriz de Adjacência:** Útil para verificar conexões diretas rapidamente (`O(1)`). Implementada expandindo dinamicamente linhas e colunas conforme novos locais são adicionados.
    * **Lista de Adjacência:** Eficiente para memória em mapas grandes e esparsos.

2.  **Manipulação do Mapa:**
    * `adicionarVertice(nome)`: Cria um novo local e redimensiona a matriz.
    * `adicionarAresta(origem, destino, custo)`: Cria uma rota de mão dupla entre dois locais, salvando o custo de acessibilidade em ambas as estruturas.

### Resultados da Visualização (Demonstração)

O sistema permite visualizar a estrutura do mapa. No teste realizado com 4 locais (Entrada, Praça, Prefeitura, Hospital):

* **Lista:** Mostra claramente os vizinhos. Ex: A Praça (`B`) conecta com a Entrada (`custo 2`), Prefeitura (`custo 5`) e Hospital (`custo 10`).
* **Matriz:** Exibe a tabela de custos completa, onde `0` indica ausência de conexão direta e os valores indicam o nível de dificuldade do trajeto.

## Desafio — Navegação e Caminhos Ótimos (DFS, BFS, Dijkstra)
### Entrega: 01/12

Implementação dos algoritmos clássicos para percorrer o mapa e traçar rotas.

### Busca em Profundidade (DFS)
- **Algoritmo:** `buscaDFS()` (Recursivo)
- **Uso no Acesso Já:** Exploração total de uma região, verificando conexões profundas entre bairros distantes.
- **Funcionamento:** Utiliza uma abordagem de "pilha" (via recursão) para ir o mais longe possível em um ramo antes de voltar (backtracking).

### Busca em Largura (BFS)
- **Algoritmo:** `buscaBFS()` (Iterativo com Fila `deque`)
- **Uso no Acesso Já:** Encontrar locais que estão a uma certa "distância de saltos" (ex: quais locais estão a 2 ruas daqui?), independentemente do custo da acessibilidade.
- **Funcionamento:** Utiliza uma Fila para explorar o grafo em "camadas" ou ondas concêntricas a partir da origem.

### Algoritmo de Dijkstra (O Roteirizador)
- **Algoritmo:** `dijkstra()` (Com Fila de Prioridade `heapq`)
- **Uso no Acesso Já:** **Funcionalidade Principal.** Encontra a rota mais acessível (menor custo total) entre dois pontos, evitando rotas com barreiras (peso alto) em favor de rotas adaptadas (peso baixo).
- **Funcionamento:** Mantém uma tabela de custos mínimos e usa um *Min-Heap* para expandir sempre o caminho mais promissor. Reconstrói o caminho final voltando do destino à origem.

### Resultados da Navegação (Demonstração)

O `main.py` simula um cenário onde ir direto da "Praça" ao "Hospital" tem um custo alto (10 - calçada ruim), mas existe um desvio pela "Prefeitura" com custo baixo (5 + 1).

* **DFS e BFS:** Mapearam com sucesso todos os nós conectados (`A -> B -> C -> D`).
* **Dijkstra (Resultado Real):**
    * O algoritmo ignorou o caminho direto (Custo 12).
    * Encontrou o desvio acessível: **`['A: Entrada', 'B: Praça', 'C: Prefeitura', 'D: Hospital']`**
    * **`Custo Total de Acessibilidade: 8`**

## Desafio — Otimização de Caminho e Processo - Gráfico Avançado
### Entrega: 19/12

Nesta fase final, o "Acesso Já" ganha capacidades de Gestão Urbana, utilizando algoritmos avançados para resolver problemas complexos de infraestrutura e planejamento.

### Árvore Geradora Mínima (MST)

- **Algoritmo:** `boruvkaMST()` (Algoritmo de Borůvka)
- **Cenário no Acesso Já:** A prefeitura precisa conectar todos os pontos de acessibilidade da cidade gastando o mínimo possível em reformas de calçadas.
- **Funcionamento:** O algoritmo trabalha em fases. Inicialmente, cada vértice é considerado uma "árvore" isolada (componente). Em cada passo, para cada componente, o algoritmo encontra a aresta mais barata que a conecta a um componente diferente e une as duas. O processo repete até sobrar apenas uma grande árvore conectando a cidade toda.

### Coloração de Grafos

- **Algoritmo:** `coloracaoWelchPowell()` (Heurística Gulosa)
- **Cenário no Acesso Já:** Agendamento de manutenção. Ruas adjacentes (vizinhas) não podem ser fechadas para obras no mesmo dia para evitar o caos no trânsito.
- **Funcionamento:** Atribui "cores" (dias) aos locais. Locais conectados recebem cores diferentes. O algoritmo ordena os vértices pelo grau (número de conexões) e tenta atribuir a primeira cor disponível que não gere conflito com os vizinhos.

### Ordenação Topológica

- **Algoritmo:** `ordenacaoTopologica()` (Algoritmo de Kahn)
- **Cenário no Acesso Já:** Planejamento de uma obra de acessibilidade (ex: Construção de uma Rampa). Certas tarefas (como "Comprar Material") dependem de outras ("Aprovar Projeto") e devem ser executadas em ordem.
- **Funcionamento:** Utiliza um Grafo Direcionado (DAG). Identifica tarefas sem dependências (grau de entrada 0), executa-as, remove-as do grafo (virtualmente) e libera as próximas tarefas que agora ficaram sem dependências.

# Análise de Complexidade (Otimização Avançada)

### Árvore Geradora Mínima (Borůvka): `O(E log V)`
- Eficiente para processamento paralelo. Reduz o número de componentes pela metade a cada passo, convergindo rapidamente.

### Coloração (Welch-Powell): `O(V^2 + E)`
- Algoritmo guloso. A ordenação dos vértices leva `O(V log V)`, mas a atribuição de cores pode verificar muitos vizinhos no pior caso.

### Ordenação Topológica (Kahn): `O(V + E)`
- Linear. Visita cada vértice e cada aresta exatamente uma vez. Muito rápido e ideal para resolução de dependências em projetos.

---

# Resultados da Otimização (Demonstração)

O `main.py` executa cenários práticos de gestão, obtendo os seguintes resultados:

### MST (Reforma de Baixo Custo):
- **Custo Mínimo calculado:** 8.
- **Rotas selecionadas:** `A <-> B`, `B <-> C`, `C <-> D`.
- *O algoritmo evitou inteligentemente a rota cara B <-> D (Custo 10), preferindo o desvio mais barato.*

### Coloração (Manutenção):
- **Agendamento realizado em 3 dias (cores).**
- *Garantia de que nenhum local vizinho (ex: Praça e Prefeitura) tenha manutenção no mesmo dia.*

### Ordenação Topológica (Obra da Rampa):
- **Cronograma lógico gerado:**
`['1. Aprovar Projeto', '2. Comprar Material', '3. Demolição', '4. Construir Rampa', '5. Pintura', '6. Inauguração']`
