def recursive_solution(x, speed, position):
    if x == position:
        return ""

    if x == position + speed:
        return "A"
    sequence = ""
    while x > position + speed:
        sequence += "A"
        position += speed
        speed *= 2

    left_before = x - position
    left_after = position + speed - x
    if left_after < left_before:
        if x == position + speed:
            sequence += "A"
            return sequence

        sequence += "AR"
        position += speed
        x = position + position - x
        speed = 1
        sequence += recursive_solution(x, speed, position)
    else:
        sequence += "RR"
        speed = 1
        sequence += recursive_solution(x, speed, position)
    return sequence


def smallest_instruction(x):  # напевно краще було б зробити динамічним
    # програмуванням, але я зробив жадіком алгоритмом(може бути не завжди
    # правильним). Складність буде лінійна
    if x == 0:
        return ""
    if x < 0:
        result = "R"
        x *= -1
    else:
        result = ""
    speed = 1
    result += recursive_solution(x, speed, 0)

    return recursive_solution(x, speed, 0)


if __name__ == '__main__':
    print(smallest_instruction(3))  # поки працює правильно

