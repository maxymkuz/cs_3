arr_2 = [2, 3, 4, 6, 11]


def similar_elements(arr1, arr2):
    idx1, idx2 = 0, 0

    while idx1 < len(arr1) and idx2 < len(arr2):

        if arr1[idx1] < arr2[idx2]:
            idx1 += 1
        elif arr1[idx1] > arr2[idx2]:
            idx2 += 1
        else:
            print(arr1[idx1])
            idx2 += 1
            idx1 += 1
    return None


def fibonacci_array(n):
    fibonacci = [1, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return fibonacci[::-1]


def fibonacci_search(array, elem):
    fibonacci = fibonacci_array(len(array))
    return recursive_search(fibonacci, 1, array, elem, fibonacci[0])


def recursive_search(fibonacci, fibonacci_idx, array, elem, idx):
    # print(idx, fibonacci[fibonacci_idx])
    if idx >= len(array):
        if fibonacci_idx >= len(fibonacci):
            return False
        idx -= fibonacci[fibonacci_idx]
        fibonacci_idx += 1
        return recursive_search(fibonacci, fibonacci_idx, array, elem, idx)

    if array[idx] == elem:
        return True
    elif fibonacci_idx >= len(fibonacci):
        return False
    elif array[idx] >= elem:
        idx -= fibonacci[fibonacci_idx]
    else:
        idx += fibonacci[fibonacci_idx]
    fibonacci_idx += 1
    return recursive_search(fibonacci, fibonacci_idx, array, elem, idx)


arr_1 = [1, 3, 5, 6, 9, 11]
if __name__ == '__main__':
    print(fibonacci_search(arr_1, 1))
