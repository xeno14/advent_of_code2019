import numpy as np
from typing import *


def parse(s: str):
    lines = s.strip().split("\n")
    res = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                res.append((x, y))
    return res


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def diff(x, y):
    return x[0]-y[0], x[1]-y[1]


def mul(x, n):
    return x[0]*n, x[1]*n


def normalize(v):
    g = np.gcd(v[0], v[1])
    return v[0]//g, v[1]//g


def dot(x, y):
    return x[0]*y[0] + x[1]*y[1]


def sort_key(d):
    d = np.array(d, dtype=np.float)
    d /= np.linalg.norm(d)
    if d[0] >= 0:
        return dot(d, (0, -1))
    else:
        return -100000 + dot(d, (0, 1))


def laser(pos, asteroids: set):
    ds = {normalize(diff(a, pos)) for a in asteroids if a != pos}
    ds = list(ds)
    ds = sorted(ds, key=sort_key, reverse=True)

    res = []
    for d in ds:
        for n in range(1, 1000):
            p = add(pos, mul(d, n))
            if p in asteroids:
                res.append(p)
                break
    return res


def solve(pos, asteroids):
    asteroids = set(asteroids)
    cnt = 0
    while len(asteroids) != 1:
        to_remove = laser(pos, asteroids)
        for a in to_remove:
            asteroids.remove(a)
            cnt += 1
            if cnt == 200:
                return a[0]*100 + a[1]


def main():
    assert diff((3, 2), (1, 1)) == (2, 1)
    assert normalize((4, 2)) == (2, 1)
    assert solve((11, 13), parse("""
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
""")) == 802

    with open("input/day10.txt") as f:
        s = f.read()
    print(solve((22, 19), parse(s)))


if __name__ == '__main__':
    main()
