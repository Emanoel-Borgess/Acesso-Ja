import modulo1_buscas
import random
import modulo2_huffman


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

if __name__ == "__main__":
    main()