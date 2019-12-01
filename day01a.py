

def mass2fuel(mass: int) -> int:
    return mass // 3 - 2


def main():
    assert mass2fuel(12) == 2
    assert mass2fuel(1969) == 654

    with open("./input/day1a.txt") as f:
        mass = [int(x) for x in f.readlines()]

    ans = sum(map(mass2fuel, mass))
    print(ans)


if __name__ == '__main__':
    main()