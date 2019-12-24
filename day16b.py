import numpy as np


def parse(s: str) -> np.array:
    return np.array([int(x) for x in s.strip()] * 10000, dtype=np.int)


def solve(v: np.array, repeat=100):
    head = int("".join(map(str, v[:7])))
    dim = v.shape[0]
    assert head >= dim//2
    v = v[dim//2+1:]
    dim = v.shape[0]
    head -= dim
    for step in range(repeat):
        # the back half of matrix is upper triangular matrix filled with 1
        # which is equivalent to cumsum
        cumsum = np.cumsum(v[::-1])[::-1]
        v = np.abs(cumsum) % 10
    return "".join(map(str, v[head-2:head+6]))


assert solve(parse("03036732577212944063491565474664")) == "84462026"
assert solve(parse("02935109699940807407585447034323")) == "78725270"
print(solve(parse(open("input/16.txt").read())))
