import numpy as np


def parse(s: str) -> np.array:
    s = s.strip().replace("\n", "")
    return np.array([c == "#" for c in s], dtype=int)


def build_mtx(n):
    mtx = np.zeros((n*n, n*n), dtype=int)
    for i in range(mtx.shape[0]):
        pattern = [1,0,0,0,1,0,1,0,0,0,1]
        if i-5 < 0:
            l = 0
            pattern = pattern[5-i:]
        else:
            l = i-5
        if i+5 >= mtx.shape[1]:
            r = mtx.shape[1]
            pattern = pattern[:r-l]
        else:
            r = i+6
        mtx[i, l:r] = pattern
        if (i+1)%5==0 and i+1<mtx.shape[0]:
            mtx[i, i+1] = 0
        if (i+1)%5==1 and i-1>=0:
            mtx[i, i-1] = 0
    return mtx


W = np.array([2**i for i in range(25)], dtype=int)


def calc_rate(world):
    return np.sum(world * W)


def visualize(world):
    for i in range(5):
        line = "".join(["#" if x == 1 else "." for x in world[i*5:i*5+5]])
        print(line)


def solve(s, max_loop=None):
    world = parse(s)
    mtx = build_mtx(5)
    seen = {calc_rate(world)}
    t = 0
    # visualize(world)
    while True:
        if max_loop and t >= max_loop:
            break
        adj = mtx.dot(world)
        adj_arr = adj.reshape((-1,))
        next_world = np.zeros(world.shape, dtype=world.dtype)

        # still live
        next_world[(world == 1) & (adj_arr == 1)] = 1

        # born
        next_world[(world == 0) & (adj_arr == 1)] = 1
        next_world[(world == 0) & (adj_arr == 2)] = 1

        world = next_world

        rate = calc_rate(world)
        if rate in seen:
            return rate
        seen.add(rate)
        t += 1


def main():
    assert calc_rate(parse("""
.....
.....
.....
#....
.#...
""")) == 2129920
    assert solve("""
....#
#..#.
#..##
..#..
#....
""") == 2129920
    with open("input/24.txt") as f:
        s = f.read()
    print(solve(s))


if __name__ == '__main__':
    main()