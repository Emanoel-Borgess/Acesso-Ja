import modulo1_buscas
import random
import modulo2_huffman
import modulo3_grafos
import modulo4_pd


def linha():
    print("\n============================================================")


def titulo(texto):
    linha()
    print(texto)
    linha()


def main():

    titulo("PROJETO ACESSO JÁ - SISTEMA DE ANÁLISE DE ACESSIBILIDADE")

    print("\nEste sistema demonstra vários algoritmos clássicos da Computação")
    print("aplicados a um cenário de acessibilidade urbana.")

# ============================================================
# DESAFIO 1
# ============================================================

    titulo("DESAFIO 1 - BUSCA EM REGISTROS DESORGANIZADOS")

    print("Situação:")
    print("Temos vários pontos de interesse cadastrados no sistema,")
    print("mas eles não estão organizados.")

    lista_pois_baguncados = [
        "POI_rampa_01",
        "POI_banco_05",
        "POI_escada_99",
        "POI_farmacia_02",
        "POI_9876",
        "POI_hospital_central"
    ]

    alvo_poi = "POI_hospital_central"

    print("\nLista atual de registros:")
    print(lista_pois_baguncados)

    print("\nObjetivo:")
    print("Encontrar:", alvo_poi)

    print("\nAlgoritmo utilizado: BUSCA SEQUENCIAL")
    print("Esse algoritmo percorre a lista elemento por elemento.")

    posicao, comparacoes = modulo1_buscas.busca_sequencial(
        lista_pois_baguncados, alvo_poi
    )

    print("\nResultado da busca:")

    if posicao != -1:
        print(f"O elemento foi encontrado na posição {posicao}")
    else:
        print("Elemento não encontrado")

    print(f"Total de comparações realizadas: {comparacoes}")

    print("\nConclusão:")
    print("Busca Sequencial tem complexidade O(n).")
    print("Isso significa que quanto maior a lista, mais lenta pode ficar.")

# ============================================================
# DESAFIO 2
# ============================================================

    titulo("DESAFIO 2 - COMPARAÇÃO DE ALGORITMOS DE BUSCA")

    print("Agora vamos analisar uma situação diferente.")
    print("Temos uma lista de CEPs já ordenada.")

    lista_ceps_ordenados = sorted(random.sample(range(10000, 99999), 100))
    alvo_cep = lista_ceps_ordenados[75]

    print("\nQuantidade de CEPs na lista:", len(lista_ceps_ordenados))
    print("CEP que queremos encontrar:", alvo_cep)

    print("\nPrimeiro usaremos BUSCA BINÁRIA.")

    print("Esse algoritmo divide a lista ao meio a cada passo.")

    posicao_bin, comps_bin = modulo1_buscas.busca_binaria(
        lista_ceps_ordenados, alvo_cep
    )

    print("\nResultado da busca binária:")
    print("Posição encontrada:", posicao_bin)
    print("Comparações realizadas:", comps_bin)

    print("\nAgora vamos simular quanto a busca sequencial demoraria.")

    posicao_seq, comps_seq = modulo1_buscas.busca_sequencial(
        lista_ceps_ordenados, alvo_cep
    )

    print("\nResultado da busca sequencial:")
    print("Comparações necessárias:", comps_seq)

    print("\nComparação final:")
    print(f"Busca Binária: {comps_bin} comparações")
    print(f"Busca Sequencial: {comps_seq} comparações")

    print("\nConclusão:")
    print("Busca Binária é muito mais eficiente em listas ordenadas.")
    print("Complexidade: O(log n)")

# ============================================================
# DESAFIO 3
# ============================================================

    titulo("DESAFIO 3 - ANÁLISE DE RELATOS DE USUÁRIOS")

    print("Agora vamos analisar relatos de usuários sobre acessibilidade.")

    texto_relatos = """
    Fui ao Cafe 101 e a rampa estava ok, mas ao chegar na porta, havia um degrau enorme.
    No dia seguinte, tentei o Parque Central. A calcada no caminho estava com muito buraco.
    A prefeitura precisa arrumar esse buraco logo!
    O Museu da Cidade e impossivel: tem uma escada na entrada e outra escada para o banheiro.
    """

    texto_limpo = texto_relatos.replace("\n", " ").strip()

    print("\nTexto analisado:")
    print(texto_limpo)

    print("\nAlgoritmo utilizado: Rabin-Karp")
    print("Ele busca padrões dentro de textos usando hashing.")

    padroes = ["degrau", "buraco", "escada"]

    for padrao in padroes:

        print(f"\nProcurando ocorrências da palavra: {padrao}")

        posicoes = modulo1_buscas.rabin_karp(texto_limpo, padrao)

        if posicoes:
            print("Encontrado nas posições:")
            for p in posicoes:
                print("-", p)
        else:
            print("Nenhuma ocorrência encontrada")

# ============================================================
# HUFFMAN
# ============================================================

    titulo("MÓDULO 2 - COMPRESSÃO DE DADOS (HUFFMAN)")

    print("Agora vamos aplicar compressão de dados ao texto (Texto usado foi o anterior).")

    texto_original = texto_limpo

    texto_comprimido, arvore = modulo2_huffman.comprimir(texto_original)

    texto_descomprimido = modulo2_huffman.descomprimir(
        texto_comprimido, arvore
    )

    tamanho_original = len(texto_original) * 8
    tamanho_comprimido = len(texto_comprimido)

    print("\nTamanho original do texto:", tamanho_original, "bits")
    print("Tamanho após compressão:", tamanho_comprimido, "bits")

    reducao = 100 * (1 - tamanho_comprimido / tamanho_original)

    print("Redução de espaço:", round(reducao, 2), "%")

    print("\nVerificação de integridade:")
    print("O texto descomprimido é igual ao original?",
          texto_original == texto_descomprimido)

# ============================================================
# GRAFOS
# ============================================================

    titulo("MÓDULO 3 - MODELAGEM DO MAPA COM GRAFOS")

    print("Agora vamos representar a cidade usando um grafo.")

    mapa = modulo3_grafos.Grafo()

    print("\nCriando locais do mapa...")

    mapa.adicionarVertice("A: Entrada")
    mapa.adicionarVertice("B: Praça")
    mapa.adicionarVertice("C: Prefeitura")
    mapa.adicionarVertice("D: Hospital")

    print("Conectando rotas entre os locais...")

    mapa.adicionarAresta("A: Entrada", "B: Praça", 2)
    mapa.adicionarAresta("B: Praça", "C: Prefeitura", 5)
    mapa.adicionarAresta("B: Praça", "D: Hospital", 10)
    mapa.adicionarAresta("C: Prefeitura", "D: Hospital", 1)

    print("\nEstrutura do grafo:")

    mapa.imprimirListaAdj()
    mapa.imprimirMatrizAdj()

# DFS

    print("\nExecutando DFS (Busca em Profundidade)")
    mapa.buscaDFS("A: Entrada")
    print("\n")

# BFS

    print("\nExecutando BFS (Busca em Largura)")
    mapa.buscaBFS("A: Entrada")
    print("\n")

# Dijkstra

    print("\nCalculando menor caminho usando Dijkstra")

    caminho, custo = mapa.dijkstra("A: Entrada", "D: Hospital")

    print("Melhor caminho encontrado:")
    print(caminho)

    print("Custo total de acessibilidade:", custo)

# ============================================================
# OTIMIZAÇÃO
# ============================================================

    titulo("OTIMIZAÇÃO DO SISTEMA")

    print("Aplicando algoritmo de Árvore Geradora Mínima (Boruvka)")

    arestas, custo = mapa.boruvkaMST()

    print("\nCusto mínimo para conectar toda a cidade:", custo)

    print("\nTrechos escolhidos:")
    for origem, destino, custo in arestas:
        print(origem, "<->", destino, "| custo:", custo)

    print("\nAplicando coloração de grafos para planejar manutenção")

    cores = mapa.coloracaoWelchPowell()

    for local, dia in cores.items():
        print(local, "-> manutenção no dia", dia)

# ============================================================
# ORDENACAO TOPOLOGICA
# ============================================================

    print("\nPlanejando etapas da construção de uma rampa acessível")

    projeto = modulo3_grafos.Grafo()

    projeto.adicionarVertice("1. Aprovar Projeto")
    projeto.adicionarVertice("2. Comprar Material")
    projeto.adicionarVertice("3. Demolição")
    projeto.adicionarVertice("4. Construir Rampa")
    projeto.adicionarVertice("5. Pintura")
    projeto.adicionarVertice("6. Inauguração")

    projeto.adicionarDependencia("1. Aprovar Projeto", "2. Comprar Material")
    projeto.adicionarDependencia("1. Aprovar Projeto", "3. Demolição")
    projeto.adicionarDependencia("2. Comprar Material", "4. Construir Rampa")
    projeto.adicionarDependencia("3. Demolição", "4. Construir Rampa")
    projeto.adicionarDependencia("4. Construir Rampa", "5. Pintura")
    projeto.adicionarDependencia("5. Pintura", "6. Inauguração")

    ordem = projeto.ordenacaoTopologica()

    print("\nOrdem correta das etapas da obra:")

    for etapa in ordem:
        print(etapa)

# ============================================================
# PROGRAMACAO DINAMICA
# ============================================================

    titulo("MÓDULO 4 - BUSCA INTELIGENTE")

    locais = mapa.vertices

    print("\nLocais cadastrados no sistema:")
    print(locais)

    entrada_usuario = "Hospitla"

    print("\nUsuário buscou por:", entrada_usuario)

    print("Aplicando algoritmo de distância de edição (Levenshtein)")

    sugestao, custo = modulo4_pd.corretor_busca_inteligente(
        entrada_usuario, locais
    )

    print("\nResultado da busca inteligente:")

    if custo == 0:
        print("Local encontrado:", sugestao)

    elif custo <= 5:
        print("Local não encontrado.")
        print("Talvez você quis dizer:", sugestao)
        print("Custo de transformação:", custo)

    else:
        print("Nenhuma correspondência próxima encontrada.")


if __name__ == "__main__":
    main()