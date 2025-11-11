import random

# Busca sequêncial

def busca_sequencial(lista, alvo):
    comparacoes = 0

    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == alvo:
            return i, comparacoes        
    return -1, comparacoes

# Busca binária

def busca_binaria(lista_ordenanda, alvo):
    comparacoes = 0
    inicio = 0
    fim = len(lista_ordenanda) -1

    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        valor_do_meio = lista_ordenanda[meio]
        if valor_do_meio == alvo:
            return meio, comparacoes
        elif valor_do_meio < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes

#### Adicionando o Rabin Karp
# Rabin Karp

def rabin_karp(texto, padrao):
    n = len(texto)
    m = len(padrao)

    if m > n:
        return[]
    
    d = 256
    q = 101
    h = 1
    for _ in range(m - 1):
        h = (h * d) % q

    hash_padrao = 0
    hash_janela_atual = 0

    for i in range(m):
        hash_padrao = (d * hash_padrao + ord(padrao[i])) % q
        hash_janela_atual = (d * hash_janela_atual + ord(texto[i])) % q

    posicoes_encontradas = []

    for i in range(n - m + 1):
        if hash_padrao == hash_janela_atual:
            if texto[i : i+m] == padrao:
                posicoes_encontradas.append(i)
        if i < n - m:
            hash_letra_saindo = (ord(texto[i]) * h) % q
            hash_janela_atual = (hash_janela_atual - hash_letra_saindo + q) % q
            hash_janela_atual = (hash_janela_atual * d) % q
            hash_janela_atual = (hash_janela_atual + ord(texto[i+m])) % q

    return posicoes_encontradas


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

    posicao, comparacoes = busca_sequencial(lista_pois_baguncados, alvo_poi)

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

    posicao_bin, comps_bin = busca_binaria(lista_ceps_ordenados, alvo_cep)

    if posicao_bin != -1:
        print(f"--- Resultado (Binária) ---")
        print(f"O alvo '{alvo_cep}' está na posição {posicao_bin}.")
        print(f"Total de comparações: {comps_bin}")
    else:
        print(f"O alvo '{alvo_cep}' não foi encontrado.")
        print(f"Total de comparações: {comps_bin}")

    print("\nAgora, vamos ver quanto a Sequencial demoraria para achar o MESMO CEP...")
    
    posicao_seq, comps_seq = busca_sequencial(lista_ceps_ordenados, alvo_cep)
    
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
        posicoes = rabin_karp(texto_limpo, padrao)
        
        if posicoes:
            print(f"O padrão '{padrao}' foi encontrado nas seguintes posições (índices):")
            for p in posicoes:
                print(f"  - Posição {p}")
        else:
            print(f"O padrão '{padrao}' não foi encontrado.")
            
    print("==========================================================")

if __name__ == "__main__":
    main()