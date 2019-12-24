from day9 import *

from collections import defaultdict


def get_inputs():
    res = []
    for i in range(50):
        for j in range(50):
            res.append((i, j))
    return res


def main():
    with open("input/19.txt") as f:
        data = [int(x) for x in f.read().strip().split(",")]

    ans = 0
    for pos in get_inputs():
        _, v = interpret(data, inputs=pos)
        ans += v[0]
        print(pos, v)
    print(ans)



if __name__ == '__main__':
    main()
