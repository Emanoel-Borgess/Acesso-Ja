# Projeto: "Acesso Já: O Roteirizador Urbano Acessível"
## Aluno: Emanoel R. Borges


## Módulo 1: Busca de Dados (Sequencial e Binária) (Entrega 04/11)

Este módulo implementa os algoritmos de Busca Sequencial e Binária, conforme solicitado na Etapa 2 do projeto. Os cenários foram adaptados ao tema "Acesso Já" para simular os desafios de lidar com dados de acessibilidade urbana.

### Desafio 1: Busca Sequencial (Registros Desorganizados)

* **Algoritmo:** `busca_sequencial()`
* **Cenário no "Acesso Já":** Simula a busca por um "Ponto de Interesse" (POI) específico (ex: "POI_hospital_central") dentro de uma lista de registros.
* **Funcionamento:** A função varre a lista, item por item (do índice 0 até o fim), contando cada comparação. Ela para assim que encontra o alvo ou chega ao fim da lista.

### Desafio 2: Busca Binária (Catálogos Ordenados)

* **Algoritmo:** `busca_binaria()`
* **Cenário no "Acesso Já":** Simula a busca por um CEP específico dentro de um catálogo de CEPs que veio devidamente ordenado. Isso é usado para verificar rapidamente a existência de um CEP em nossa base de dados.
* **Funcionamento:** A função usa a abordagem de "dividir para conquistar". Ela olha o meio da lista: se o alvo for maior, joga a metade esquerda fora; se for menor, joga a metade direita fora. Ela repete isso até encontrar o alvo ou o espaço de busca desaparecer.

## Busca de Dados em texto (Rabin-Karp) (Entrega 11/11)

### Desafio 3: Busca em Texto (Rabin-Karp)

* **Algoritmo:** `rabin_karp()`
* **Cenário no "AcessoJá":** Simula o "Desafio 3: Decifrando os Relatos de Usuários". O algoritmo analisa um "Tomo Antigo" (um texto longo com relatos de usuários) para encontrar "Marcas de Corrupção" (palavras-chave de inacessibilidade como "escada", "buraco" e "degrau").
* **Funcionamento:** O algoritmo implementa um **rolling hash** (hash deslizante). Em vez de comparar letras, ele compara "números mágicos" (hashes) da janela de texto com o hash do padrão. Isso é muito rápido. Quando os hashes batem, ele faz uma verificação final letra por letra para evitar falsos positivos (colisões). No meu teste, ele identificou com sucesso todas as ocorrências das palavras-chave nos relatos.

---

### Análise de Complexidade (A Comparação)

O programa principal (`main()`) demonstra a diferença de eficiência:

* **Busca Sequencial (Pior Caso): O(n)**
    * No nosso teste, para encontrar o alvo na posição 75 de uma lista de 100 CEPs, foram necessárias **76 comparações**. No pior caso, se o alvo fosse o último, seriam 100 comparações.
* **Busca Binária (Pior Caso): O(log n)**
    * Para encontrar o *mesmo alvo* (posição 75), a Busca Binária precisou de apenas **7 comparações**. Isso prova que ela é exponencialmente mais rápida para lidar com grandes volumes de dados *ordenados*.
* **Rabin-Karp (Caso Médio): O(n+m)**
    * O algoritmo consegue analisar um texto de `n` caracteres para encontrar um padrão de `m` caracteres de forma muito eficiente (quase linear). É imensamente mais rápido do que uma busca por força bruta ($O(n*m)$).