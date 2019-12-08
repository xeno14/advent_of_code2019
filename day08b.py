from day08a import read_image

import numpy as np


def find_first(l):
    for c in l:
        if c != 2:
            return c
    return 2


def join_layers(image: np.array):
    res = np.zeros(image.shape[1:], dtype=int)
    _, w, h = image.shape
    for i in range(w):
        for j in range(h):
            res[i, j] = find_first(image[:, i, j])
    return res


def main():
    with open("input/day8.txt") as f:
        ser = f.read().strip()
        raw_image = read_image(ser, 6, 25)

    image = join_layers(raw_image)

    for row in image:
        print(" ".join([" " if c == 0 else "@" for c in row]))


if __name__ == '__main__':
    main()
