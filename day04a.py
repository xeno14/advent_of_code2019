def loop_for_pairs(digits):
    return zip(digits[:-1], digits[1:])


def any_adjacent_same(digits):
    for x, y in loop_for_pairs(digits):
        if x == y:
            return True
    else:
        return False


def is_ascending(digits):
    return sorted(digits) == digits
    # or O(N) implementation
    # for x, y in loop_for_pairs(digits):
    #     if x > y:
    #         return False
    # return True


def isvalid(n):
    digits = n_to_digits(n)
    return is_ascending(digits) and any_adjacent_same(digits)


def n_to_digits(n):
    return [int(c) for c in str(n)]


def main():
    assert any_adjacent_same([1,2,3,4,4,6])
    assert not any_adjacent_same([1,2,3,4,5,6])
    assert is_ascending([1, 2, 3, 4, 4, 6])
    assert not is_ascending([1, 2, 1, 4, 4, 6])
    assert isvalid(111123)
    assert isvalid(111111)
    assert not isvalid(223450)
    assert not isvalid(123789)

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
