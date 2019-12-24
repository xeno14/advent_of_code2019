import numpy as np


def parse(s: str) -> np.array:
    lines = [line.strip() for line in s.strip().split("\n")]
    nx = len(lines[0])
    ny = len(lines)
    nlevel = 601
    grid = np.zeros((nlevel, nx, ny), dtype=int)
    for y in range(ny):
        for x in range(nx):
            grid[nlevel//2, x, y] = lines[y][x] == "#"
    return grid


def count_adjacent(grid, level, x, y):
    count = 0
    # left
    if x == 0:
        count += grid[level-1, 1, 2]
    elif x == 1:
        count += grid[level,x-1,y]
    elif x == 2 and y != 2:
        count += grid[level, x-1, y]
    elif x == 3:
        if y == 2:
            count += grid[level+1, 4, :].sum()
        else:
            count += grid[level, x-1, y]
    elif x == 4:
        count += grid[level,x-1,y]
    # right
    if x == 0:
        count += grid[level, x+1, y]
    elif x == 1:
        if y == 2:
            count += grid[level+1, 0, :].sum()
        else:
            count += grid[level, x + 1, y]
    elif x == 2 and y != 2:
        count += grid[level, x+1, y]
    elif x == 3:
        count += grid[level, x+1, y]
    elif x == 4:
        count += grid[level-1, 3, 2]
    # top
    if y == 0:
        count += grid[level-1, 2, 1]
    elif y == 1:
        count += grid[level, x, y-1]
    elif y == 2 and x != 2:
        count += grid[level, x, y-1]
    elif y == 3:
        if x == 2:
            count += grid[level+1, :, 4].sum()
        else:
            count += grid[level, x, y - 1]
    elif y == 4:
        count += grid[level, x, y - 1]
    # bottom
    if y == 0:
        count += grid[level, x, y + 1]
    elif y == 1:
        if x == 2:
            count += grid[level+1, :, 0].sum()
        else:
            count += grid[level, x, y + 1]
    elif y == 2 and x != 2:
        count += grid[level, x, y + 1]
    elif y == 3:
        count += grid[level, x, y+1]
    elif y == 4:
        count += grid[level-1, 2, 3]
    return count


def evolve(grid, step):
    nlevel, nx, ny = grid.shape
    next_grid = np.zeros(grid.shape, dtype=grid.dtype)
    mid = nlevel//2
    for level in range(mid-step-1, mid+step+2):
        for x in range(nx):
            for y in range(ny):
                if x == 2 and y == 2:
                    continue
                n = count_adjacent(grid, level, x, y)
                if grid[level, x, y] == 1:
                    next_grid[level, x, y] = n == 1
                else:
                    next_grid[level, x, y] = n == 1 or n == 2
    # make sure center is empty
    next_grid[:, 2, 2] = 0
    return next_grid


def solve(s, steps):
    grid = parse(s)
    nlevel, _, _ = grid.shape
    for t in range(1, steps+1):
        print(t)
        grid = evolve(grid, t)

        # print("------------------ %d ------------------" % t)
        # center = nlevel // 2
        # for level in range(center-t, center+t+1):
        #     layer = grid[level]
        #     if layer.sum()==0: continue
        #     print("level", level-center)
        #     print(grid[level].T)
    return grid.sum()


def main():
    #     s = """
    # ##.##
    # #.##.
    # #...#
    # ##.#.
    # ####.
    #     """
    assert solve("""
....#
#..#.
#.?##
..#..
#....
""", steps=10) == 99
    with open("input/24.txt") as f:
        s = f.read()
    print(solve(s, steps=200))


if __name__ == '__main__':
    main()