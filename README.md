# Projeto: “Acesso Já: O Roteirizador Urbano Acessível”
## Aluno: Emanoel R. Borges

# Módulo 1 — Busca de Dados (Sequencial, Binária e Texto)
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

### Rabin-Karp (caso mádio): `O(n + m)`
- O algoritmo consegue analisar um texto de n caracteres para encontrar um padrão de m caracteres de forma muito eficiente (quase linear). É imensamente mais rápido do que uma busca por força bruta ($O(n*m)$).

---

# Módulo 2 — Otimização de Recursos (Compressão de Huffman)
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