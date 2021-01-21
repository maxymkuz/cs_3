import queue
import copy


def get_index(row, column, n):
    return row * n + column


def initialize_edges(array, n):
    graph = [set() for i in range(2 * n ** 2 + 2)]
    source = 2 * n ** 2
    sink = 2 * n ** 2 + 1
    for row in range(n):
        for column in range(n):
            index = get_index(row, column, n)

            # if connected to source
            if array[row][column] == 1:
                graph[source].add((index, 1))
            else:  # Making additional vertex
                graph[index].add((index + n ** 2, 1))

            if row % (n - 1) == 0 or column % (n - 1) == 0:  # If це край
                graph[index] = {(sink, 1)}
            else:
                if array[row][column] == 1:  # Link to second
                    graph[index].add((index + n ** 2, 1))
                graph[index + n ** 2] = {
                    (get_index(row - 1, column, n), 1),
                    (get_index(row + 1, column, n), 1),
                    (get_index(row, column - 1, n), 1),
                    (get_index(row, column + 1, n), 1)}
    return graph


def bfs(source, g_f, sink, n):
    visited = [False for i in range(2 * n ** 2 + 2)]
    q = queue.Queue()
    q.put(source)
    parents = [-1 for i in range(2 * n ** 2 + 2)]
    path = []
    got_to_sink = False
    counter = 0
    while not q.empty() and counter < 100000:
        counter += 1
        cur_vertex = q.get()
        visited[cur_vertex] = True
        for edge in g_f[cur_vertex]:
            if not visited[edge[0]]:  # TODO
                parents[edge[0]] = cur_vertex
                if edge[0] == sink:  # we have found a path
                    got_to_sink = True
                    break
                # print(edge[0])
                q.put(edge[0])
        if got_to_sink:
            break

    if not got_to_sink:
        return []

    path.append(sink)
    while parents[path[0]] != -1:
        path.insert(0, parents[path[0]])
    return path


def augment(flow, g_f, graph, path):
    for edge in range(len(path) - 1):
        current_vertex = path[edge]
        next_vertex = path[edge + 1]
        if (next_vertex, 1) in graph[current_vertex]:  # forward edge
            g_f[current_vertex].remove((next_vertex, 1))
            g_f[next_vertex].add((current_vertex, 1))
            flow[current_vertex].add(next_vertex)
        else:
            g_f[current_vertex].remove((next_vertex, 1))
            flow[current_vertex].discard(next_vertex)
    return g_f


def traverse_backwards(source, sink, flow, n):
    paths = []

    for cur_vertex in flow[source]:
        mid_res = [source]
        x = cur_vertex
        counter = 0

        while x != sink and counter < 500000:
            counter += 1

            mid_res.append(x)
            # print(list(flow[x]))
            x = list(flow[x])[0]

        mid_res.append(x)
        paths.append(mid_res)
    return paths


def escape_problem(array):
    n = len(array)
    if n > 100:
        return []
    source = 2 * n ** 2
    sink = 2 * n ** 2 + 1

    # print(source, sink)

    graph = initialize_edges(array, n)
    g_f = copy.deepcopy(graph)
    flow = [set() for i in range(len(graph))]

    path = bfs(source, g_f, sink, n)
    while path:
        g_f = augment(flow, g_f, graph, path)
        path = bfs(source, g_f, sink, n)

    # print(flow)
    final = traverse_backwards(source, sink, flow, n)
    for i in range(len(final)):
        final[i] = [(final[i][j] // n, final[i][j] % n) for j in
                    range(len(final[i])) if final[i][j] < n * n]
    return final


def read_json(filename):
    import json
    with open(filename, 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    m = [[0, 0, 0],
         [1, 1, 1],
         [0, 1, 0]]
    # print(escape_problem(m))
    tests = read_json("test_06.json")
    i = 0
    for test in tests:
        # i += 1
        # if i != 1:
        #     continue
        n = test['size']
        m_test = [[0 for _ in range(n)] for _ in range(n)]
        for point in test['points']:
            m_test[point[0]][point[1]] = 1
        for i in range(len(m_test)):
            print(m_test[i])
        print(len(test['flows']), test['flows'])
        paths = escape_problem(m_test)

        print(len(paths), paths)
        print("_" * 80)
