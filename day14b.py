from day14a import *


def calc_ore(formulas, nfuel):
    reserve = defaultdict(int)
    return rec(nfuel, "FUEL", reserve, formulas)


TRI = 1000000000000


def solve2(formulas):
    l = 1
    r = 5586022
    # binary search
    while True:
        mid = (l+r)//2
        ore = calc_ore(formulas, mid)
        if r-l <= 1:
            if ore <= TRI:
                return mid
            else:
                return l
        if ore > TRI:
            r = mid
        if ore < TRI:
            l = mid


def main():
    assert solve2(parse("""
171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX
""")) == 460664

    print(solve2(parse(open("input/day14.txt").read())))


if __name__ == '__main__':
    main()