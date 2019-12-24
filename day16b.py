import numpy as np


def parse(s: str) -> np.array:
    return np.array([int(x) for x in s.strip()] * 10000, dtype=np.int)


def solve(v: np.array, repeat=100):
    # the back half of matrix is upper triangular matrix filled with 1
    # which is equivalent to cumsum
    head = int("".join(map(str, v[:7])))
    dim = v.shape[0]
    # make sure head is in back half
    assert head >= dim//2
    v = v[head:]
    for step in range(repeat):
        v = np.abs(np.cumsum(v[::-1])[::-1]) % 10
    return "".join(map(str, v[:8]))


assert solve(parse("03036732577212944063491565474664")) == "84462026"
assert solve(parse("02935109699940807407585447034323")) == "78725270"
print(solve(parse(open("input/16.txt").read())))
