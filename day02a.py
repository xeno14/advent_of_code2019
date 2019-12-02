def add(x, y):
    return x+y


def mul(x, y):
    return x*y


def next_step(pos, data):
    if data[pos] == 99:
        return -1, data
    op = add if data[pos] == 1 else mul
    data[data[pos+3]] = op(data[data[pos+1]], data[data[pos+2]])
    return pos+4, data


def interpret(data):
    pos = 0
    while pos != -1:
        pos, data = next_step(pos, data)
    return data


def main():
    assert next_step(0, [1, 0, 0, 0]) == (4, [2, 0, 0, 0])
    assert next_step(0, [2, 3, 0, 3]) == (4, [2, 3, 0, 6])
    assert interpret([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert interpret([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    with open("./input/day2.txt") as f:
        data = [int(x) for x in f.read().split(",")]
    # before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
    data[1] = 12
    data[2] = 2
    data = interpret(data)
    print(data[0])


if __name__ == '__main__':
    main()



