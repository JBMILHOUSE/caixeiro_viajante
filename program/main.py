import os
import re
import math
import numpy as np

def selecionar_arquivo_2(diretorio):
    # lista todos arquivos no diretorio
    arquivo = os.listdir(diretorio)
    for i, filename in enumerate(arquivo):
       print(f'arquivos disponiveis {i}: {filename}')

    while True:
        try:
            posicao_arquivo = int(input('Informe o número do arquivo que deseja selecionar: '))
            if 0 <= posicao_arquivo < len(arquivo):
                return os.path.join(diretorio, arquivo[posicao_arquivo])
            else:
                print('Número informado inválido, tente novamente.')
        except ValueError:
            print('Entrada inválida, por favor insirá uma número')

"""
leitura teste de instancia (coordenadas)
passo 1: criando função de ler instancia passando
como parâmetro o arquivo selecionado.
passo 2: criar um vetor vázio de inst
passo 3: abrir e ler contéudo dentro do arquivo
passo 4: laço for criando para percorrer o conteudo de arquivo
passo 5: variaveis criadas i, x, y percorrendo cada indice dentro
do arquivo selecionado, i representa o número de cidades<n_cidades>
x e y representam as coordenadas de cada cidade.
passo 6: adiciona ao vetor<inst> as coordenadas de x e y.
passo 7: retorna o vetor<inst>
"""
def ler_instancia(caminho_path):
    inst = []
    with open(caminho_path, 'r') as arquivo:
        leitores = arquivo.readlines()
        for leitor in leitores:
            i, x, y = map(int, leitor.split())
            inst.append((x, y))
    return inst

"""
extração do conteudo do arquivo selecionado

"""
def ler_todas_instancias(caminho_path):
    match = re.match(r'mTSP-n(\d+)-m(\d+)', os.path.basename(caminho_path))
    if match:
        n_cidades, n_caixeiros = map(int, match.groups())
        return n_cidades, n_caixeiros
    else:
        raise ValueError(f'O nome arquivo {caminho_path} não está no formato esperado.')

"""
função para calcular de distância entre cidades passando
as coordenadas cidadeX e cidadeY como parâmetro
"""
def calcular_distancia_entre_cidades(coordX, coordY):
    return math.sqrt((coordY[0] - coordX[0]) ** 2 + (coordY[1] - coordX[1]) ** 2)

def distancia_total(rota, cidades):
    total_distance = 0
    for cidade in range(len(rota) - 1):
        total_distance += calcular_distancia_entre_cidades(cidades[rota[cidade]], cidades[rota[i+1]])
    total_distance += calcular_distancia_entre_cidades(cidades[rota[-1]], cidades[rota[0]])
    return total_distance

# print(f'testando funções calculo entre cidade e distancia total {distancia_total(n_cidades, n_caixeiros)}')

"""
Rota do vizinho mais próximo
"""
def vizinho_mais_heuristic(n_cidades, coordenadas):
    tour = [0]
    cidades_nao_visitadas = list(range(1, n_cidades))

    while cidades_nao_visitadas:
        cidade_atual = tour[-1]
        cidade_proxima = None
        minima_distancia = float('inf')

        for city in cidades_nao_visitadas:
            distance_cidade = calcular_distancia_entre_cidades(coordenadas[cidade_atual], coordenadas[city])
            if distance_cidade < minima_distancia:
                minima_distancia = distance_cidade
                cidade_proxima = city 
        
        tour.append(cidade_proxima)
        cidades_nao_visitadas.remove(cidade_proxima)
    
    tour.append(tour[0])
    return tour

def farthest_neighbor_heuristic(n_cidades, coordenadas):
    tour = [0]
    cidades_nao_visitadas = list(range(1, n_cidades))

    while cidades_nao_visitadas:
        cidade_atual = tour[-1]
        cidade_distante = 0
        distante_distancia = None

        for city in cidades_nao_visitadas:
            distance_cidade = calcular_distancia_entre_cidades(coordenadas[cidade_atual], coordenadas[city])
            if distance_cidade > cidade_distante:
                cidade_distante = distance_cidade
                distante_distancia = city

        tour.append(distante_distancia)
        cidades_nao_visitadas.remove(distante_distancia)
    
    tour.append(tour[0])
    return tour

"""
função para distribuir cidades entre os caixeiros

"""

def encontrar_cidade_mais_proxima(ponto, cidades):
    return min(cidades, key=lambda x:calcular_distancia_entre_cidades(ponto, x))

def calcular_centroide(coordenadas_cidades):
    coordenadas_cidades = np.array(coordenadas_cidades)
    return np.mean(coordenadas_cidades, axis=0)

def distribuir_cidades(coordenadas,  n_caixeiros):
    n_cities = len(coordenadas)
    cidade_inicial = coordenadas[0] # definindo a cidade incial de onde os caixeiros sairão e para onde retornarão

    #Ordena as cidades pela distância ao centroide
    cidades_ordenadas = sorted(coordenadas[1:], key=lambda x: calcular_distancia_entre_cidades(x, cidade_inicial))
     
    #Distribuir as cidades entre os caixeiros
    rotas_por_caixeiro = [[] for _ in range(n_caixeiros)]
    for i, cidade in enumerate(cidades_ordenadas):
        caixeiro = i % n_caixeiros
        # if len(rotas_por_caixeiro[caixeiro]) == 0:
        #     # Garantir que o caixeiro comece na cidade mais próxima do centroide
        #     rotas_por_caixeiro[caixeiro].append(cidade_inicial)
        rotas_por_caixeiro[caixeiro].append(cidade)
        # else:
        #     rotas_por_caixeiro[caixeiro].append(cidade)
    
    # Garantir que todos os caixeiros retornem à mesma inicial
    for rota in rotas_por_caixeiro:
        rota.insert(0, cidade_inicial)
        rota.append(cidade_inicial)
        
    return rotas_por_caixeiro

diretorio = "instances\\"
caminho_path = selecionar_arquivo_2(diretorio)
coordenadas = ler_instancia(caminho_path)

n_cidades, n_caixeiros = ler_todas_instancias(caminho_path)

rota_vizinho_mais_proximo = vizinho_mais_heuristic(n_cidades, coordenadas)
rota_vizinho_distante = farthest_neighbor_heuristic(n_cidades, coordenadas)

print(f'nome arquivo selecionado {caminho_path}')
print(f'coordenadas de x e y {coordenadas}')
print(f'número de cidades {n_cidades} e número de caixeiros {n_caixeiros}')
# print(type(n_cidades))

print(f'caminho encontrado pela heuristica do vizinho mais proximo: {rota_vizinho_mais_proximo}')
# print(f'distancia total do caminho vizinho mais próximo {distancia_total(rota_vizinho_mais_proximo)}')
print(f'caminho encontrado pela heuristica do vizinho mais distante : {rota_vizinho_distante}')
# print(f'distancia total do caminho vizinho mais distante {distancia_total(rota_vizinho_distante)}')

rota_por_caixeiros = distribuir_cidades(coordenadas, n_caixeiros)
for i, rota in enumerate(rota_por_caixeiros):
    print(f'Caixeiro {i+1}: {rota}')