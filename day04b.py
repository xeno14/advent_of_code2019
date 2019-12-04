from day04a import loop_for_pairs, is_ascending, n_to_digits


def any_adjacent_same_but_not_wider(digits):
    from collections import defaultdict
    cnt = defaultdict(int)
    for x, y in loop_for_pairs(digits):
        if x == y:
            cnt[x] += 1
    return 1 in cnt.values()


def isvalid(n):
    digits = n_to_digits(n)
    return is_ascending(digits) and any_adjacent_same_but_not_wider(digits)


def main():
    assert any_adjacent_same_but_not_wider([1, 2, 3, 4, 4, 6])
    assert not any_adjacent_same_but_not_wider([1, 2, 3, 4, 5, 6])
    assert not any_adjacent_same_but_not_wider([1, 2, 3, 4, 4, 4])
    assert isvalid(112233)
    assert not isvalid(123444)
    assert isvalid(111122)

    ans = 0
    for n in range(271973, 785961+1):
        if isvalid(n):
            print(n, "is valid")
            ans += 1
        else:
            print(n, "is not valid")
    print(ans)


if __name__ == '__main__':
    main()
