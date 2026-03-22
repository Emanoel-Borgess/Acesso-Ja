import heapq
# Huffman
# compressão de dados sem perdas
# economiza espaço

class No:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

    def __lt__(self, other):
        return self.frequencia < other.frequencia
    
# Comprime relatos de usuários
def comprimir(texto):
    frequencias = {}

    for caractere in texto:
        frequencias[caractere] = frequencias.get(caractere, 0) + 1

    filaDePrioridade = []
    for caractere, frequencia in frequencias.items():
        noAtual = No(caractere, frequencia)
        heapq.heappush(filaDePrioridade, noAtual)

    while len(filaDePrioridade) > 1:
        noEsquerdo = heapq.heappop(filaDePrioridade)
        noDireito = heapq.heappop(filaDePrioridade)
        novoNoPai = No(None, noEsquerdo.frequencia + noDireito.frequencia)

        novoNoPai.esquerda = noEsquerdo
        novoNoPai.direita = noDireito

        heapq.heappush(filaDePrioridade, novoNoPai)
        
    raizDaArvore = filaDePrioridade[0]
    mapaArvore = {}

    def codigoCaminhoArvore(noAtual, codigoDoCaminho, mapaCodigo):
        if noAtual is not None:
            if noAtual.caractere is not None:
                mapaCodigo[noAtual.caractere] = codigoDoCaminho
            else:
                codigoCaminhoArvore(noAtual.esquerda, codigoDoCaminho + "0", mapaCodigo)
                codigoCaminhoArvore(noAtual.direita, codigoDoCaminho + "1", mapaCodigo)

    codigoCaminhoArvore(raizDaArvore, "", mapaArvore)
    textoCodificado = ""

    for caractere in texto:
        textoCodificado += mapaArvore[caractere]

    return textoCodificado, raizDaArvore

def descomprimir(textoCodificado, arvore):
    textoDescodificado = ""
    noAtual = arvore

    for bit in textoCodificado:
        if bit == '0':
            noAtual = noAtual.esquerda
        else:
            noAtual = noAtual.direita
        
        if noAtual.caractere is not None:
            textoDescodificado += noAtual.caractere
            noAtual = arvore

    return textoDescodificado