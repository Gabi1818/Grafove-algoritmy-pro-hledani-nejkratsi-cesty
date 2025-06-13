INF = float('inf')

graph = [
    [0, 10, INF, 3, INF, INF],
    [INF, 0, 2, INF, INF, INF],
    [INF, INF, 0, INF, INF, INF],
    [INF, INF, INF, 0, 8, INF],
    [INF, INF, INF, INF, 0, 1],
    [INF, INF, 4, INF, INF, 0]
]

def floyd_warshall_with_paths(graph):
    V = len(graph)
    dist = [row[:] for row in graph]

    # Inicializace matice předchůdců
    next_node = [[None if graph[i][j] == INF else j for j in range(V)] for i in range(V)]

    # Algoritmus Floyd-Warshall
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node

# Rekonstrukce cesty z uzlu u do v
def construct_path(u, v, next_node):
    if next_node[u][v] is None:
        return []

    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path

# Spustíme algoritmus
dist, next_node = floyd_warshall_with_paths(graph)

# Výpis vzdáleností
print("Matrice nejkratších vzdáleností:")
for row in dist:
    print(row)

# Výpis cest mezi všemi dvojicemi
print("\nKonkrétní cesty mezi uzly:")
for i in range(len(graph)):
    for j in range(len(graph)):
        if i != j:
            path = construct_path(i, j, next_node)
            if path:
                print(f"Cesta z {i} do {j}: {' → '.join(map(str, path))} (vzdálenost: {dist[i][j]})")
            else:
                print(f"Cesta z {i} do {j}: neexistuje")
