import numpy as np
from typing import *


def parse(s: str):
    lines = s.strip().split("\n")
    res = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                res.append(np.array([x, y], dtype=int))
    return res


def count(pos: np.array, asteroids: List[np.array]):
    sight = set()
    cnt = 0
    for a in asteroids:
        d = a - pos
        if np.linalg.norm(d) == 0:
            continue
        d //= np.gcd(d[0], d[1])
        d = (d[0], d[1])
        if d in sight:
            continue
        cnt += 1
        sight.add(d)
    return cnt


def solve(asteroids: List[np.array]) -> (int, Tuple[int, int]):
    ans = 0
    loc = np.array([-1, -1])
    for a in asteroids:
        cnt = count(a, asteroids)
        if cnt > ans:
            loc = a
            ans = cnt
    return ans, loc


def test_cases():
    return [
        ("""
.#..#
.....
#####
....#
...##    
""", (8, [3, 4])),
        ("""
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####    
""", (33, [5, 8])),
        ("""
#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.        
""", (35, [1, 2])),
        ("""
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
""", (210, [11, 13])),
    ]


def run_test():
    for i, (s, expected) in enumerate(test_cases()):
        res = solve(parse(s))
        cnt = res[0]
        delta = np.linalg.norm(np.array(expected[1])-res[1])
        if cnt == expected[0] and np.linalg.norm(delta) == 0:
            print("case %d passed" % i)
        else:
            print("case %d failed" % i)


def main():
    run_test()

    with open("input/day10.txt") as f:
        s = f.read()
    ans = solve(parse(s))
    print(ans)


if __name__ == '__main__':
    main()
