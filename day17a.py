from day9 import interpret

import numpy as np


SCAFFOLD = 1
ROBOT = 2

def parse_image(image):
    lines = image.strip().split("\n")
    scaffolds = []
    robo = (-100000, -100000)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                scaffolds.append((x, y, SCAFFOLD))
            if c == "^":
                robo = (x, y, ROBOT)
    return scaffolds, robo


def list2grid(pos):
    xmin = min([p[0] for p in pos])
    ymin = min([p[1] for p in pos])
    xmax = max([p[0] for p in pos])
    ymax = max([p[1] for p in pos])
    stage = np.zeros((xmax + 1 - xmin, ymax + 1 - ymin), dtype=int)
    for x, y, val in pos:
        stage[x, y] = val
    return stage


def find_intersections(grid):
    nx, ny = grid.shape
    res = []
    for x in range(1, nx-1):
        for y in range(1, ny-1):
            if grid[x,y]==SCAFFOLD and grid[x+1,y]==SCAFFOLD and grid[x-1,y]==SCAFFOLD and grid[x,y-1]==SCAFFOLD and grid[x,y+1]==SCAFFOLD:
                res.append((x,y))
    return res


def main():
    with open("input/17.txt") as f:
        data = [int(x) for x in f.read().strip().split(",")]
    _, outputs = interpret(data)
    image = "".join([str(chr(code)) for code in outputs])
    #     image = """
    # ..#..........
    # ..#..........
    # #######...###
    # #.#...#...#.#
    # #############
    # ..#...#...#..
    # ..#####...^..
    # """
    scaffolds, robo = parse_image(image)
    print(image)
    grid = list2grid(scaffolds)
    isecs = find_intersections(grid)
    ans = sum(map(lambda x: x[0]*x[1], isecs))
    print(ans)


if __name__ == '__main__':
    main()