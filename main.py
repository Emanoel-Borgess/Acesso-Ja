import modulo1_buscas
import random
import modulo2_huffman
import modulo3_grafos


def main():

    print("==========")
    print("Acesso Já")
    print("==========")

    print("\n--- Desafio 1: registros desorganizados ---")
    lista_pois_baguncados = ["POI_rampa_01", "POI_banco_05", "POI_escada_99",
        "POI_farmacia_02", "POI_9876", "POI_hospital_central"]
    
    alvo_poi = "POI_hospital_central"

    print(f"Lista de POIs bagunçada: {lista_pois_baguncados}")
    print(f"Procurando pelo alvo: {alvo_poi}\n")

    posicao, comparacoes = modulo1_buscas.busca_sequencial(lista_pois_baguncados, alvo_poi)

    if posicao != -1:
        print(f"--- Resultado (sequencial) ---")
        print(f"O alvo {alvo_poi} está na posição {posicao}.")
        print(f"Total de comparações: {comparacoes}")
    else:
        print(f"O alvo '{alvo_poi}' não foi encontrado.")
        print(f"Total de comparações: {comparacoes}")
        
    print("-----------------------------------------------------")

    print("\n--- Desafio 2: registros ordenados ---")
    lista_ceps_ordenados = sorted(random.sample(range(10000, 99999), 100))
    alvo_cep = lista_ceps_ordenados[75]
    
    print(f"Temos uma lista ordenanda de {len(lista_ceps_ordenados)} CEPs.")
    (f"Lista de CEPs: {lista_ceps_ordenados}")
    print(f"Procurando pelo alvo: '{alvo_cep}'\n")

    posicao_bin, comps_bin = modulo1_buscas.busca_binaria(lista_ceps_ordenados, alvo_cep)

    if posicao_bin != -1:
        print(f"--- Resultado (Binária) ---")
        print(f"O alvo '{alvo_cep}' está na posição {posicao_bin}.")
        print(f"Total de comparações: {comps_bin}")
    else:
        print(f"O alvo '{alvo_cep}' não foi encontrado.")
        print(f"Total de comparações: {comps_bin}")

    print("\nAgora, vamos ver quanto a Sequencial demoraria para achar o MESMO CEP...")
    
    posicao_seq, comps_seq = modulo1_buscas.busca_sequencial(lista_ceps_ordenados, alvo_cep)
    
    print(f"--- RESULTADO (Sequencial na lista ordenada) ---")
    print(f"A Busca Sequencial precisou de... {comps_seq} comparações!")
    print("\n--- CONCLUSÃO ---")
    print(f"Busca Binária: {comps_bin} comparações.")
    print(f"Busca Sequencial: {comps_seq} comparações.")
    print("A Busca Binária é bem mais eficiente! (O(log n) vs O(n))")
    print("==========================================================")

    # ---
    # !! ATUALIZAÇÃO DA MAIN !!
    # Adicionando o Desafio 3
    # ---
    
    print("\n--- Desafio 3: Decifrando os Relatos de Usuários ---")
    texto_relatos = """
    Fui ao Cafe 101 e a rampa estava ok, mas ao chegar na porta, havia um degrau enorme.
    No dia seguinte, tentei o Parque Central. A calcada no caminho estava com muito buraco.
    A prefeitura precisa arrumar esse buraco logo!
    O Museu da Cidade e impossivel: tem uma escada na entrada e outra escada para o banheiro.
    """

    padroes_para_buscar = ["degrau", "buraco", "escada"]
    
    print(f"Texto de Relatos (Tomo Antigo):\n{texto_relatos}")
    
    for padrao in padroes_para_buscar:
        print(f"--- Procurando pelo padrão: '{padrao}' ---")
        texto_limpo = texto_relatos.replace("\n", " ").strip()
        
        posicoes = modulo1_buscas.rabin_karp(texto_limpo, padrao)
        
        if posicoes:
            print(f"O padrão '{padrao}' foi encontrado nas seguintes posições (índices):")
            for p in posicoes:
                print(f"  - Posição {p}")
        else:
            print(f"O padrão '{padrao}' não foi encontrado.")
            
    print("==========================================================")

    # !! ATUALIZAÇÃO DA MAIN !!!
    print("\n--- Huffman ---")

    # MESMO texto do Desafio 3
    texto_original_relatos = texto_relatos.replace("\n", " ").strip()

    print(f"Texto Original: '{texto_original_relatos}'")
    texto_comprimido, arvore_huffman = modulo2_huffman.comprimir(texto_original_relatos)
    texto_descomprimido = modulo2_huffman.descomprimir(texto_comprimido, arvore_huffman)

    tamanho_original_bits = len(texto_original_relatos) * 8 # 8 bits por caractere (ASCII)
    tamanho_comprimido_bits = len(texto_comprimido)

    print(f"Tamanho Original (bits): {tamanho_original_bits}")
    print(f"Tamanho Comprimido (bits): {tamanho_comprimido_bits}")

    reducao = 100 * (1 - tamanho_comprimido_bits / tamanho_original_bits)
    print(f"Redução de espaço: {reducao:.2f}%")
    print("\n--- Verificação de Integridade ---")
    print(f"Textos são idênticos? {texto_original_relatos == texto_descomprimido}")
    print("==========================================================")

# Atualização da main (Módulo 3)
    print("\n==========================================================")
    print("--- Módulo 3: O Mapa do Mundo (Grafos) ---")
    mapa = modulo3_grafos.Grafo()
    print("Criando locais...")
    mapa.adicionarVertice("A: Entrada")
    mapa.adicionarVertice("B: Praça")
    mapa.adicionarVertice("C: Prefeitura")
    mapa.adicionarVertice("D: Hospital")
    print("Conectando rotas...")
    mapa.adicionarAresta("A: Entrada", "B: Praça", 2)
    
    mapa.adicionarAresta("B: Praça", "C: Prefeitura", 5)
    
    mapa.adicionarAresta("B: Praça", "D: Hospital", 10)
    
    mapa.adicionarAresta("C: Prefeitura", "D: Hospital", 1)

    mapa.imprimirListaAdj()
    mapa.imprimirMatrizAdj()

# Atualização da main (Entrega dia 01/12/2025)
    print("\n--- Testando DFS (Exploração Profunda) ---")
    print("Começando da Entrada (A)...")
    mapa.buscaDFS("A: Entrada")
    print("FIM")

    print("\n--- Testando BFS (Exploração em Camadas) ---")
    mapa.buscaBFS("A: Entrada")
    print("FIM")


    print("\n--- Testando Dijkstra (Menor Custo de Acessibilidade) ---")
    print("Calculando melhor rota de 'A: Entrada' para 'D: Hospital'...")
    
    caminho, custo_total = mapa.dijkstra("A: Entrada", "D: Hospital")
    
    print(f"Melhor Caminho: {caminho}")
    print(f"Custo Total de Acessibilidade: {custo_total}")

# Atualização da main (Entrega dia 19/12/2025)
    print("\n==========================================================")
    print("--- Módulo 3: O Mapa do Mundo (Grafos) ---")
    
    mapa = modulo3_grafos.Grafo()

    print("Criando locais...")
    mapa.adicionarVertice("A: Entrada")
    mapa.adicionarVertice("B: Praça")
    mapa.adicionarVertice("C: Prefeitura")
    mapa.adicionarVertice("D: Hospital")

    print("Conectando rotas...")
    mapa.adicionarAresta("A: Entrada", "B: Praça", 2)
    mapa.adicionarAresta("B: Praça", "C: Prefeitura", 5)
    mapa.adicionarAresta("B: Praça", "D: Hospital", 10)
    mapa.adicionarAresta("C: Prefeitura", "D: Hospital", 1)

    mapa.imprimirListaAdj()
    mapa.imprimirMatrizAdj()

    print("\n--- Testando DFS (Exploração Profunda) ---")
    print("Começando da Entrada (A)...")
    mapa.buscaDFS("A: Entrada")

    print("\n--- Testando BFS (Exploração em Camadas) ---")
    mapa.buscaBFS("A: Entrada")

    print("\n--- Testando Dijkstra (Menor Custo de Acessibilidade) ---")
    print("Calculando melhor rota de 'A: Entrada' para 'D: Hospital'...")
    
    caminho, custo_total = mapa.dijkstra("A: Entrada", "D: Hospital")
    
    print(f"Melhor Caminho: {caminho}")
    print(f"Custo Total de Acessibilidade: {custo_total}")

    print("\n==========================================================")
    print("--- Módulo 3 (Final): Otimização Avançada ---")

    print("\n[MST - Algoritmo de Borůvka] Planejando rede de reformas de menor custo total:")
    mstArestas, custoMst = mapa.boruvkaMST()
    
    print(f"Custo Mínimo para conectar toda a cidade: {custoMst}")
    print("Rotas escolhidas para reforma:")
    for origem, destino, custo in mstArestas:
        print(f"  - Reformar trecho {origem} <--> {destino} (Custo: {custo})")

    print("\n[Coloração] Agendando manutenção para evitar bloqueios simultâneos em ruas vizinhas:")
    agendamento = mapa.coloracaoWelchPowell()
    for local, dia in agendamento.items():
        print(f"  - {local}: Manutenção no Dia {dia}")

    print("\n[Ordenação Topológica] Planejamento da Obra de uma Rampa:")
    
    projeto_obra = modulo3_grafos.Grafo()
    projeto_obra.adicionarVertice("1. Aprovar Projeto")
    projeto_obra.adicionarVertice("2. Comprar Material")
    projeto_obra.adicionarVertice("3. Demolição")
    projeto_obra.adicionarVertice("4. Construir Rampa")
    projeto_obra.adicionarVertice("5. Pintura")
    projeto_obra.adicionarVertice("6. Inauguração")

    projeto_obra.adicionarDependencia("1. Aprovar Projeto", "2. Comprar Material") 
    projeto_obra.adicionarDependencia("1. Aprovar Projeto", "3. Demolição")      
    projeto_obra.adicionarDependencia("2. Comprar Material", "4. Construir Rampa")
    projeto_obra.adicionarDependencia("3. Demolição", "4. Construir Rampa")        
    projeto_obra.adicionarDependencia("4. Construir Rampa", "5. Pintura")
    projeto_obra.adicionarDependencia("5. Pintura", "6. Inauguração")

    ordem_execucao = projeto_obra.ordenacaoTopologica()
    print("Ordem correta de execução da obra:")
    print(ordem_execucao)

if __name__ == "__main__":
    main()