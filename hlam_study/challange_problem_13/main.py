import pandas as pd
from math import log


def transition_matrix_from_list(array):
    matrix = [[0, 0], [0, 0]]
    num_items = len(array)

    for i in range(num_items - 1):
        matrix[array[i - 1]][array[i]] += 1

    # for i in range(2):
    #     for j in range(2):
    #         matrix[i][j] = matrix[i][j] / num_items

    return matrix


def calculate_beta(x, y):
    log_result = 0
    for i in range(1, x + 1):
        log_result += log(i, 2)
    for i in range(1, y + 1):
        log_result += log(i, 2)
    for i in range(1, x + y + 1):
        log_result -= log(i, 2)
    return log_result


def identify_distribution(matrix):
    mc = calculate_beta(matrix[0][0], matrix[0][1]) + calculate_beta(
        matrix[1][1], matrix[1][0])
    bernoulli = calculate_beta(matrix[0][0] + matrix[0][1], matrix[1][0] +
                               matrix[1][1])
    result = mc - bernoulli
    if result > 100:  # just by deduction
        print("The input is formed out of markov chain")
    else:
        print("That's probably a sequence of bernoulli r.v.")


if __name__ == '__main__':
    data = pd.read_csv("data.csv")

    matrix1 = transition_matrix_from_list(data.iloc[0].values)
    matrix2 = transition_matrix_from_list(data.iloc[1].values)

    identify_distribution(matrix1)
    identify_distribution(matrix2)
