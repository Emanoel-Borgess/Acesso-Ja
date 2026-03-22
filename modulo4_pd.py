
# Usa Programação Dinâmica (Tabulação) para calcular o custo mínimo de transformar uma string em outra através de inserção, remoção ou substituição.
def calcular_distancia_edicao(termo_usuario, termo_banco_dados):
    tamanho_usuario = len(termo_usuario)
    tamanho_banco = len(termo_banco_dados)
    tabela_distancias = [[0 for _ in range(tamanho_banco + 1)] for _ in range(tamanho_usuario + 1)]

    for linha in range(tamanho_usuario + 1):
        tabela_distancias[linha][0] = linha
        
    for coluna in range(tamanho_banco + 1):
        tabela_distancias[0][coluna] = coluna

    for linha in range(1, tamanho_usuario + 1):
        for coluna in range(1, tamanho_banco + 1):
            if termo_usuario[linha - 1] == termo_banco_dados[coluna - 1]:
                tabela_distancias[linha][coluna] = tabela_distancias[linha - 1][coluna - 1]
            else:
                custo_remocao = tabela_distancias[linha - 1][coluna]
                custo_insercao = tabela_distancias[linha][coluna - 1]
                custo_substituicao = tabela_distancias[linha - 1][coluna - 1]
                tabela_distancias[linha][coluna] = 1 + min(custo_remocao, custo_insercao, custo_substituicao)
    return tabela_distancias[tamanho_usuario][tamanho_banco]

# Compara a entrada do usuário com os vértices do Grafo e sugere o local mais próximo matematicamente, tratando erros de digitação.
def corretor_busca_inteligente(termo_digitado, lista_locais_conhecidos):
    local_mais_proximo = None
    menor_distancia_encontrada = float('inf')
    for local in lista_locais_conhecidos:
        distancia_atual = calcular_distancia_edicao(termo_digitado.lower(), local.lower())
        if distancia_atual < menor_distancia_encontrada:
            menor_distancia_encontrada = distancia_atual
            local_mais_proximo = local        
    return local_mais_proximo, menor_distancia_encontrada