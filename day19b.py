from day9 import *

from collections import defaultdict



def get_inputs():
    res = []
    for i in range(50):
        for j in range(50):
            res.append((i, j))
    return res


def drone(data, x, y):
    _, outputs = interpret(data, inputs=[x, y])
    return outputs[0]


def main():
    with open("input/19.txt") as f:
        data = [int(x) for x in f.read().strip().split(",")]

    # space = dict()
    # for pos in get_inputs():
    #     v = drone(data, pos[0], pos[1])
    #     space[pos] = v
    # from util import draw_stage
    # draw_stage(space, {0: ".", 1: "#"})

    N = 100
    for y in range(N, 10*N):
        print(y)
        x = int(y)
        while drone(data, x, y) == 0:
            x += 1
        x0 = x

        x = x0 + N
        while drone(data, x, y) == 1:
            x += 1
        if drone(data, x-N, y) == 0:
            continue
        x1 = x - N
        if drone(data, x1, y+N-1) == 1 and drone(data, x1, y+N) == 0:
            pos = (x1, y)
            break
    print(pos)
    print(pos[0]*10000 + pos[1])




    # ans = 0
    # space = dict()
    # for pos in get_inputs():
    #     _, v = interpret(data, inputs=pos)
    #     ans += v[0]
    #     space[pos] = v[0]
    # from util import draw_stage
    # draw_stage(space, {0: ".", 1: "#"})



if __name__ == '__main__':
    main()
