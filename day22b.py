from functools import partial


# define inverse functions
def newstack(j, p):
    return p-j-1


def cut(j, p, n):
    while n < 0:
        n += p
    i = j - p + n
    if i < 0:
        i += p
    if i < n:
        return i
    else:
        return j + n


def incremental(j, p, n):
    # Fermat's little theorem
    return j * pow(n, p-2, p) % p


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
    return deals[::-1]


def apply(i, p, deals):
    for deal in deals:
        i = deal(i, p)
    return i


def main():
    assert [cut(j, 7, 3) for j in range(7)] == [3,4,5,6,0,1,2]
    assert [cut(j, 7, -2) for j in range(7)] == [5,6,0,1,2,3,4]
    assert [incremental(j, 5, 3) for j in range(5)]

    with open("input/22.txt") as f:
        deals = parse(f.read())
    assert apply(7744, 10007, deals) == 2019

    P = 119315717514047
    # P = 9221
    REPEAT = 101741582076661
    # REPEAT = 1000000
    i = 2020
    for t in range(REPEAT):
        if t % 10000 == 0:
            print("%d/%d*100=%f" % (t, REPEAT, t//REPEAT*100))
        i = apply(i, P, deals)
        print(i)
        if i == 2020:
            print("looped", t+1)
            break


if __name__ == '__main__':
    main()
