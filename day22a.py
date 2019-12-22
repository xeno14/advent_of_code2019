from functools import partial


def newstack(i, l):
    return l-i-1


def cut(i, l, n):
    if i<n:
        return l-n+i
    else:
        return i-n


def incremental(i, l, n):
    return i * n % l


def parse(s: str):
    deals = []
    for line in s.strip().split("\n"):
        if line.startswith("cut"):
            n = int(line.split()[-1])
            deals.append(partial(cut, n=n))
        elif line.startswith("deal into new stack"):
            deals.append(newstack)
        elif line.startswith("deal with increment"):
            n = int(line.split()[-1])
            deals.append(partial(incremental, n=n))
        else:
            raise RuntimeError("unknown")
    return deals


def apply(i, l, deals):
    for deal in deals:
        i = deal(i, l)
    return i


DECK10 = list(range(10))


def main():
    with open("input/22.txt") as f:
        deals = parse(f.read())
    print(apply(2019, 10007, deals))


if __name__ == '__main__':
    main()
