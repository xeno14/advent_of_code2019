import numpy as np

from day9 import *


def stage(outputs):
    return [(outputs[i], outputs[i+1], outputs[i+2]) for i in range(0, len(outputs), 3)]


def itoc(i):
    if i == 0:
        return " "
    if i == 1:
        return "W"
    if i == 2:
        return "#"
    if i == 3:
        return "-"
    if i == 4:
        return "o"


def draw_stage(tiles):
    xmax = max([t[0] for t in tiles])
    ymax = max([t[1] for t in tiles])
    stage = np.zeros((xmax+1, ymax+1), dtype=int)
    for t in tiles:
        stage[t[0], t[1]] = t[2]

    for y in range(stage.shape[1]):
        s = "".join([itoc(stage[x, y]) for x in range(stage.shape[0])])
        print(s)


def main():
    with open("input/day13.txt") as f:
        data = [int(x) for x in f.read().strip().split(",")]
    _, outputs = interpret(data)

    tiles = stage(outputs)
    draw_stage(tiles)


if __name__ == '__main__':
    main()