from collections import deque


def get_pos(code, pos, n, data):
    res = []
    for i in range(n):
        c = code%10
        code //= 10
        if c == 0:
            p = data[pos+i]
        else:
            p = pos+i
        res.append(p)
    return res


def next_step(pos, data, inputs):
    leader = data[pos]
    pos += 1

    opcode = leader%100
    poscode = leader//100

    if opcode == 99:
        return -1, data, None
    if opcode == 1:
        p1, p2, p3 = get_pos(poscode, pos, 3, data)
        pos += 3
        data[p3] = data[p1] + data[p2]
        return pos, data, None
    if opcode == 2:
        p1, p2, p3 = get_pos(poscode, pos, 3, data)
        pos += 3
        data[p3] = data[p1] * data[p2]
        return pos, data, None
    if opcode == 3:  # input
        p1 = data[pos]
        pos += 1
        try:
            data[p1] = next(inputs)
        except StopIteration:
            return pos-1, data, None  # skip
        return pos, data, None
    if opcode == 4:
        p1 = data[pos]
        pos += 1
        return pos, data, data[p1]
    if opcode == 5:  # jump-if-true
        p1, p2 = get_pos(poscode, pos, 2, data)
        pos += 2
        if data[p1] != 0:
            pos = data[p2]
        return pos, data, None
    if opcode == 6:  # jump-if-false
        p1, p2 = get_pos(poscode, pos, 2, data)
        pos += 2
        if data[p1] == 0:
            pos = data[p2]
        return pos, data, None
    if opcode == 7:  # less than
        p1, p2, p3 = get_pos(poscode, pos, 3, data)
        pos += 3
        data[p3] = int(data[p1] < data[p2])
        return pos, data, None
    if opcode == 8:  # equal to
        p1, p2, p3 = get_pos(poscode, pos, 3, data)
        pos += 3
        data[p3] = int(data[p1] == data[p2])
        return pos, data, None
    else:
        raise RuntimeError("unknown opcode %d" % opcode)


def visualize(pos, data):
    print("%4d:\t" % pos, end="")
    for i in range(len(data)):
        if i == pos:
            print("[", end="")
        print(data[i], end="")
        if i == pos:
            print("]", end="")
        print(" ", end="")
    print()


def interpret(data, inputs=None, verbose=False):
    if inputs is None:
        inputs = []
    inputs = iter(inputs)
    outputs = []
    pos = 0
    while pos != -1:
        if verbose:
            visualize(pos, data)
        pos, data, o = next_step(pos, data, inputs)
        if o is not None:
            outputs.append(o)
    return data, outputs


def main():
    assert interpret([1002,4,3,4,33])[0] == [1002,4,3,4,99]
    assert interpret([1101,100,-1,4,0])[0] == [1101,100,-1,4,99]
    assert interpret([3,9,8,9,10,9,4,9,99,-1,8], inputs=[0])[1] == [0]
    assert interpret([3,9,8,9,10,9,4,9,99,-1,8], inputs=[8])[1] == [1]
    assert interpret([3,9,7,9,10,9,4,9,99,-1,8], inputs=[7])[1] == [1]
    assert interpret([3,9,7,9,10,9,4,9,99,-1,8], inputs=[8])[1] == [0]
    assert interpret([3,9,7,9,10,9,4,9,99,-1,8], inputs=[9])[1] == [0]
    assert interpret([3,3,1108,-1,8,3,4,3,99], inputs=[0])[1] == [0]
    assert interpret([3,3,1108,-1,8,3,4,3,99], inputs=[8])[1] == [1]
    assert interpret([3,3,1107,-1,8,3,4,3,99], inputs=[7])[1] == [1]
    assert interpret([3,3,1107,-1,8,3,4,3,99], inputs=[8])[1] == [0]
    assert interpret([3,3,1107,-1,8,3,4,3,99], inputs=[9])[1] == [0]
    assert interpret([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], inputs=[0])[1] == [0]
    assert interpret([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], inputs=[10])[1] == [1]
    assert interpret([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], inputs=[0])[1] == [0]
    assert interpret([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], inputs=[10])[1] == [1]

    # ??? crashes
    # large_example = [
    #     3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
    #     1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
    #     999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99
    # ]
    # assert interpret(large_example, inputs=[8], verbose=True)[1] == [999]

    with open("./input/day5.txt") as f:
        data = [int(x) for x in f.read().split(",")]

    # part1
    print("part1", interpret(list(data), inputs=[1])[1][-1])

    # part2
    print("part2", interpret(list(data), inputs=[5])[1][-1])


if __name__ == '__main__':
    main()