from day01a import mass2fuel


def calcfuel(mass):
    fuel = 0
    while True:
        mass = mass2fuel(mass)
        if mass <= 0:
            break
        fuel += mass
    return fuel


def main():
    assert calcfuel(1969) == 966
    assert calcfuel(100756) == 50346

    with open("./input/day1a.txt") as f:
        mass = [int(x) for x in f.readlines()]
    ans = sum(map(calcfuel, mass))
    print(ans)


if __name__ == '__main__':
    main()