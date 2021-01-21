n = 100
not_visited = [True for i in range(n)]


def dfs_find_max_len(cur_vertex, edges):
    not_visited[cur_vertex] = False

    adjacent_vertices = []
    for edge in edges:
        if cur_vertex in edge:
            if edge[0] == cur_vertex and not_visited[edge[1] - 1]:
                adjacent_vertices.append(edge[1])
            elif edge[1] == cur_vertex and not_visited[edge[0] - 1]:
                adjacent_vertices.append(edge[0])

    if len(adjacent_vertices) == 0:
        return 0

    max_length = -1
    for vertex in adjacent_vertices:
        max_length = max([dfs_find_max_len(vertex, edges) + 1, max_length])
    return max_length


def roots(n, edges):  # O(n**2 + nm)
    root_length = [-1 for i in range(n)]  # O(n)
    for vertex in range(1, n + 1):  # O(n)
        root_length[vertex - 1] = dfs_find_max_len(vertex, edges)  # O(n + m)

    min_height = min(root_length)
    result = [i for i in range(n) if root_length[i] == min_height] # O(n)
    return result


