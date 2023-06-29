from typing import List


def count_max_sum(stairs: List[int], n: int) -> int:
    if n == 1:
        return stairs[0]
    if n == 2:
        return max(stairs[1], stairs[0] + stairs[1])
    d = [stairs[0], max(stairs[1], stairs[0] + stairs[1])]
    for i in range(2, n):
        d_i = max(d[-2], d[-1]) + stairs[i]
        d.append(d_i)
    return d[-1]


def main():
    n = int(input())
    stairs = [int(x) for x in input().split()]
    result = count_max_sum(stairs, n)
    print(result)


if __name__ == '__main__':
    main()
