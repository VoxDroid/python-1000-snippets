# sample1.py
# Basic Dijkstra as shown in README

import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

if __name__ == '__main__':
    graph = {
        0: [(1, 4), (2, 8)],
        1: [(0, 4), (2, 2), (3, 5)],
        2: [(0, 8), (1, 2), (3, 5)],
        3: [(1, 5), (2, 5)]
    }
    print('distances', dijkstra(graph, 0))
