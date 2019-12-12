import numpy as np


def simulate(initial_pos, steps):
    n = len(initial_pos)
    x = np.zeros((n, 3), dtype=int)
    v = np.zeros((n, 3), dtype=int)

    for i, pos in enumerate(initial_pos):
        x[i,:] = pos

    for _ in range(steps):
        a = np.zeros((n, 3), dtype=int)
        for d in range(3):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    if x[i, d] < x[j, d]:
                        a[i, d] += 1
                    elif x[i, d] > x[j, d]:
                        a[i, d] -= 1
        v += a
        x += v
    return x, v


def parse(s: str):
    lines = s.strip().split("\n")
    res = []
    for line in lines:
        line = line.replace("<x=", "").replace("y=", "").replace("z=", "").replace(">", "")
        res.append([int(x.strip()) for x in line.split(",")])
    return res


def solve(initial_pos, steps):
    x, v = simulate(initial_pos, steps)
    x = np.abs(x)
    v = np.abs(v)
    return np.sum(x.sum(axis=1) * v.sum(axis=1))


def main():
    assert solve(parse("""
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
    """), 10) == 179

    with open("input/day12.txt") as f:
        initial_pos = parse(f.read())

    print(solve(initial_pos, 1000))


if __name__ == '__main__':
    main()