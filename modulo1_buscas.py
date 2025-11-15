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