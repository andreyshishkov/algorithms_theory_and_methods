from typing import List


def count_max_len(arr: List[int], n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    d = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] % arr[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    return max(d)


def main():
    n = int(input())
    arr = [int(x) for x in input().split()]

    result = count_max_len(arr, n)
    print(result)


if __name__ == '__main__':
    main()
