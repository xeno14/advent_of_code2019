from collections import defaultdict


def get_pos(code, pos, rb, n, data):
    res = []
    for i in range(n):
        c = code % 10
        code //= 10
        if c == 0:
            p = data[pos+i]
        elif c == 1:
            p = pos+i
        elif c == 2:
            p = rb+data[pos+i]
        else:
            raise ValueError("invalid pos code %d" % c)
        res.append(p)
    return res


def next_step(pos, rb, data, inputs):
    leader = data[pos]
    pos += 1

    opcode = leader%100
    poscode = leader//100

    if opcode == 99:
        return -1, rb, data, None
    if opcode == 1:
        p1, p2, p3 = get_pos(poscode, pos, rb, 3, data)
        pos += 3
        data[p3] = data[p1] + data[p2]
        return pos, rb, data, None
    if opcode == 2:
        p1, p2, p3 = get_pos(poscode, pos, rb, 3, data)
        pos += 3
        data[p3] = data[p1] * data[p2]
        return pos, rb, data, None
    if opcode == 3:  # input
        p1, = get_pos(poscode, pos, rb, 1, data)
        pos += 1
        data[p1] = next(inputs)
        return pos, rb, data, None
    if opcode == 4:
        p1, = get_pos(poscode, pos, rb, 1, data)
        pos += 1
        return pos, rb, data, data[p1]
    if opcode == 5:  # jump-if-true
        p1, p2 = get_pos(poscode, pos, rb, 2, data)
        pos += 2
        if data[p1] != 0:
            pos = data[p2]
        return pos, rb, data, None
    if opcode == 6:  # jump-if-false
        p1, p2 = get_pos(poscode, pos, rb, 2, data)
        pos += 2
        if data[p1] == 0:
            pos = data[p2]
        return pos, rb, data, None
    if opcode == 7:  # less than
        p1, p2, p3 = get_pos(poscode, pos, rb, 3, data)
        pos += 3
        data[p3] = int(data[p1] < data[p2])
        return pos, rb, data, None
    if opcode == 8:  # equal to
        p1, p2, p3 = get_pos(poscode, pos, rb, 3, data)
        pos += 3
        data[p3] = int(data[p1] == data[p2])
        return pos, rb, data, None
    if opcode == 9:
        p1, = get_pos(poscode, pos, rb, 1, data)
        rb += data[p1]
        pos += 1
        return pos, rb, data, None
    else:
        raise RuntimeError("unknown opcode %d" % opcode)


def visualize(pos, rb, data):
    print("%4d %4d:\t" % (pos, rb), end="")
    for i in range(len(data)):
        if i == pos:
            print("[", end="")
        print(data[i], end="")
        if i == pos:
            print("]", end="")
        print(" ", end="")
    print()


def build_unbound_data(data):
    res = defaultdict(int)
    for i, x in enumerate(data):
        res[i] = x
    return res


def interpret(data, inputs=None, verbose=False):
    if inputs is None:
        inputs = []
    inputs = iter(inputs)
    outputs = []
    pos = 0
    rb = 0
    data = build_unbound_data(data)
    while pos != -1:
        if verbose:
            visualize(pos, rb, data)
        pos, rb, data, o = next_step(pos, rb, data, inputs)
        if o is not None:
            outputs.append(o)
    return data, outputs


def main():
    assert interpret([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])[1] == [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    assert interpret([1102,34915192,34915192,7,4,7,99,0])[1] == [1219070632396864]
    assert interpret([104,1125899906842624,99])[1] == [1125899906842624]

    with open("./input/day9.txt") as f:
        data = [int(x) for x in f.read().split(",")]

    # part1
    print(interpret(data, inputs=[1])[1])

    # part2
    print(interpret(data, inputs=[2])[1])


if __name__ == '__main__':
    main()