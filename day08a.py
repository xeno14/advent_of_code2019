import numpy as np


def read_image(ser: str, width, height):
    digits = [int(c) for c in ser.strip()]
    return np.array(digits, dtype=int).reshape((-1, width, height))


def solve(image: np.array):
    l, w, h = image.shape
    image = image.reshape((l, w*h))
    count0 = (image == 0).sum(axis=1)
    i = np.argmin(count0)
    layer0 = image[i]
    print(layer0)
    count1 = (layer0 == 1).sum()
    count2 = (layer0 == 2).sum()
    return count1 * count2


def main():
    with open("input/day8.txt") as f:
        image = read_image(f.read(), 25, 6)
    ans = solve(image)
    print(ans)


if __name__ == '__main__':
    main()
