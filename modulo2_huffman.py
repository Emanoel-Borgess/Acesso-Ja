import heapq # Biblioteca nativa do Python para criar fila de prioridade.

class No:
    def __init__(self, caractere, frequencia): # Construtor da classe
        self.caractere = caractere  # O caractere
        self.frequencia = frequencia  # A frequência
        self.esquerda = None  # O filho da esquerda (o bit '0') None significa vazio
        self.direita = None # O filho da direita (o bit '1')

    # Ele vai ordenar pela frequência crescente
    def __lt__(self, other):
        return self.frequencia < other.frequencia
    
# Função de comprimir
def comprimir(texto):
    frequencias = {}

    for caractere in texto:
        frequencias[caractere] = frequencias.get(caractere, 0) + 1

    filaDePrioridade = []
    for caractere, frequencia in frequencias.items():
        noAtual = No(caractere, frequencia)
        heapq.heappush(filaDePrioridade, noAtual)

    while len(filaDePrioridade) > 1:
        noEsquerdo = heapq.heappop(filaDePrioridade) # Pegando os nós mais leves
        noDireito = heapq.heappop(filaDePrioridade)
        novoNoPai = No(None, noEsquerdo.frequencia + noDireito.frequencia)

        novoNoPai.esquerda = noEsquerdo
        novoNoPai.direita = noDireito

        heapq.heappush(filaDePrioridade, novoNoPai) # Colocando o novo nó na arvore e reordenando
        
    raizDaArvore = filaDePrioridade[0] # Minha árore completa
    mapaArvore = {} #Mapa para guardar os códigos da arvore

    def codigoCaminhoArvore(noAtual, codigoDoCaminho, mapaCodigo):
        if noAtual is not None: #verificando se o nó é vazio
            if noAtual.caractere is not None: # Verificando se o nó é uma folha, ou seja, se ele tem um caractere
                mapaCodigo[noAtual.caractere] = codigoDoCaminho
            else:
                codigoCaminhoArvore(noAtual.esquerda, codigoDoCaminho + "0", mapaCodigo)
                codigoCaminhoArvore(noAtual.direita, codigoDoCaminho + "1", mapaCodigo)

    codigoCaminhoArvore(raizDaArvore, "", mapaArvore)
    textoCodificado = ""

    for caractere in texto:
        textoCodificado += mapaArvore[caractere]

    return textoCodificado, raizDaArvore

# Função para descomprimir o texto
def descomprimir(textoCodificado, arvore):
    textoDescodificado = ""
    noAtual = arvore #Ponteiro para saber em qual posição estou na árvore

    for bit in textoCodificado:
        if bit == '0':
            noAtual = noAtual.esquerda
        else:
            noAtual = noAtual.direita
        
        if noAtual.caractere is not None:
            textoDescodificado += noAtual.caractere
            noAtual = arvore

    return textoDescodificado