def recursive(items, total_weight):
    weights = {0: [0, []]}

    for i in range(len(items)):
        w = items[i][1]
        v = items[i][0]
        for key in sorted(list(weights.keys()))[::-1]:
            new_weight = key + w

            if new_weight <= total_weight:
                # ignore_set.add(new_weight)
                if new_weight not in weights:
                    weights[new_weight] = [v + weights[key][0],
                                           weights[key][1] + [i]]
                else:
                    weights[new_weight] = max(
                        (weights[new_weight], [v + weights[key][0],
                                               weights[key][1] + [i]]),
                        key=lambda x: x[0])
    # print(weights)
    return weights


def knapsack(items, weight):
    x = sum((i[1] for i in items))
    if x <= weight:
        return sum((i[0] for i in items)), [i for i in range(len(items))]


    max_val = -1
    list_of_indexes = []
    weights = recursive(items, weight)
    for key in weights:
        if weights[key][0] > max_val:
            max_val, list_of_indexes = weights[key]
    return max_val, list_of_indexes


def traverse_backwards(source, sink, cur_vertex, flow):
    if cur_vertex == sink:
        return [sink]
    else:
        if cur_vertex == source:
            all_paths = []

        for next_vertex in flow[cur_vertex]:
            result = traverse_backwards(source, sink, next_vertex, flow)
            if result:
                result = [cur_vertex] + result
                if cur_vertex == source:
                    all_paths.append(result)
                else:
                    return result
        if cur_vertex == source:
            return all_paths
    return False



if __name__ == '__main__':
    print([[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10],
                    [6, 4], [5, 3], [7, 3]])
    print(knapsack([[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10],
                    [6, 4], [5, 3], [7, 3]], 20))

