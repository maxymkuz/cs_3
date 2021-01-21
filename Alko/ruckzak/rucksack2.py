def knapsack(items, weight):
    """
    :param items: list
    :param weight: int
    :return: tuple
    """
    total_value = 0
    result_items = []

    temp = {}
    # weight, value, itemlist
    temp[0] = [0, []]
    for i, item in enumerate(items):
        # print(item, i)
        keys = reversed(sorted(list(temp.keys())))
        # print(temp)
        for elem in keys:
            if elem + item[1] > weight:
                continue
            if elem + item[1] in temp:
                if temp[elem + item[1]][0] < temp[elem][0] + item[0]:
                    temp[elem + item[1]][0] = temp[elem][0] + item[0]
                    temp[elem + item[1]][1] = temp[elem][1] + [i]
            else:
                temp[elem + item[1]] = [temp[elem][0] + item[0],
                                        temp[elem][1] + [i]]
    for elem in temp:
        if temp[elem][0] > total_value:
            total_value = temp[elem][0]
            result_items = temp[elem][1]
    return total_value, result_items


if __name__ == '__main__':
    print([[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10],
                    [6, 4], [5, 3], [7, 3]])
    print(knapsack([[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10],
                    [6, 4], [5, 3], [7, 3]], 20))
