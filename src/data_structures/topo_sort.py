from collections import deque

def topo_sort(n, edges):
    graph = [[] for _ in range(n)]
    indegree = [0]*n

    for a,b in edges:
        graph[a].append(b)
        indegree[b] += 1

    q = deque()

    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    order = []

    while q:
        node = q.popleft()
        order.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return order


if __name__ == "__main__":
    #example graph with 5 nodes and 4 edges
    edges = []
    edges.append([1, 2])
    edges.append([0, 2])
    edges.append([2, 3])
    edges.append([3, 4])
    n = len(edges) + 1
    print("--------------Topo-Sort-------------")
    print(topo_sort(n, edges))