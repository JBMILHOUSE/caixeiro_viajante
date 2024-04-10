"""
 Implementação base do problema do caixeiro viajante
 desenvolvida durante as aulas de Tópicos em inteligência artificial

"""
# numero de cidade
n_cities = 17

distance = [
      [0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354, 468, 776, 662],
      [548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674, 1016, 868, 1210],
      [776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164, 1130, 788, 1552, 754],
      [696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822, 1164, 560, 1358],
      [582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708, 1050, 674, 1244],
      [274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628, 514, 1050, 708],
      [502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856, 514, 1278, 480],
      [194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320, 662, 742, 856],
      [308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662, 320, 1084, 514],
      [194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388, 274, 810, 468],
      [536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764, 730, 388, 1152, 354],
      [502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114, 308, 650, 274, 844],
      [388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194, 536, 388, 730],
      [354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0, 342, 422, 536],
      [468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536, 342, 0, 764, 194],
      [776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274, 388, 422, 764, 0, 798],
      [662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730, 536, 194, 798, 0],
]

"""
Introducao, heuristica construtiva, experimentos computacionais, instancias de teste e resultados
coordenadas -- exemplos
d(a, b) =  raiz quadrada de 2 (xA - xB) sobre 2 + (yA - yB) arredondar para cima

prazo para entrega quarta-feira da semana de que vem... deus é pai mais nao é padastro
"""

# distancia total
def get_total_distance(tour: list):
    total_distance = 0

    for city in range(n_cities - 1):
       total_distance += distance[tour[city]][tour[city + 1]]
    total_distance += distance[tour[-1]][tour[0]]

    return total_distance

# função heuristica do vizinho mais próximo
def nearest_neighbor_heuristic(): 
    #lista vazia
    tour = [0]
    # Lista de cidades não visitadas
    unvisited = list(range(1, n_cities))
    
    while unvisited:
       current_city = tour[-1]
       next_city = None
       min_distance = float('inf')

       for city in unvisited:
           if distance[current_city][city] < min_distance:
                min_distance = distance[current_city][city]
                next_city = city
           
       tour.append(next_city)
       unvisited.remove(next_city)

    tour.append(tour[0])
    return tour

#vizinho mais distante
def farthest_neighbor_heuristic(): 
    tour = [0]
    unvisited = list(range(1, n_cities))
    
    while unvisited:
       current_city = tour[-1]
       farthest_distance = 0
       farthest_city = None

       for city in unvisited:
           if distance[current_city][city] > farthest_distance:
                farthest_distance = distance[current_city][city]
                farthest_city = city
           
       tour.append(farthest_city)
       unvisited.remove(farthest_city)

    tour.append(tour[0])
    return tour
                                          

rota_nearest_neighbor = nearest_neighbor_heuristic()
rota_farthest_neighbor = farthest_neighbor_heuristic()

print('Caminho encontrado pela heurística do vizinho mais próximo: ', rota_nearest_neighbor)
print('Caminho encontrado pela heurística do vizinho mais distante: ', rota_farthest_neighbor)

print('Distância total do caminho do vizinho mais próximo: ', get_total_distance(rota_nearest_neighbor))
print('Distância total do caminho do vizinho mais distante: ', get_total_distance(rota_farthest_neighbor))