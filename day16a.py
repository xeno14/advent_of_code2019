import numpy as np


def parse(s: str) -> np.array:
    return np.array([int(x) for x in s.strip()], dtype=np.int)


def build_matrix(n: int) -> np.array:
    mtx = np.zeros((n, n), dtype=np.int)
    base_pattern = [0, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            idx = (j+1) // (i+1) % len(base_pattern)
            mtx[i, j] = base_pattern[idx]
    return mtx


def solve(v: np.array, repeat=100):
    mtx = build_matrix(len(v))
    for _ in range(repeat):
        v = mtx.dot(v)
        v = np.abs(v) % 10
    return "".join(map(str, v))[:8]


assert solve(parse("12345678"), repeat=4) == "01029498"
assert solve(parse("80871224585914546619083218645595"), repeat=100) == "24176176"
assert solve(parse("19617804207202209144916044189917"), repeat=100) == "73745418"
assert solve(parse("69317163492948606335995924319873"), repeat=100) == "52432133"
print(solve(parse(open("input/16.txt").read())))
