from typing import List


def count_lt_nums(point: int, arr: List[int], n: int) -> int:
    left, right = 0, n - 1
    if arr[left] > point:
        return 0
    if arr[right] < point:
        return n
    while left < right:
        middle = (left + right) // 2
        if arr[middle] == point:
            right = middle
        elif arr[middle] > point:
            right = middle
        else:
            left = middle + 1
    return left


def count_lq_nums(point: int, arr: List[int], n: int) -> int:
    left, right = 0, n - 1
    if arr[left] > point:
        return 0
    if arr[right] <= point:
        return n
    while left < right:
        middle = (left + right) // 2
        if arr[middle] == point:
            left = middle + 1
        elif arr[middle] > point:
            right = middle
        else:
            left = middle + 1
    return left


def count_segments(point: int, sorted_start: List[int], sorted_finish: List[int], n: int) -> int:
    lq_start_num = count_lq_nums(point, sorted_start, n)
    lt_finish_num = count_lt_nums(point, sorted_finish, n)
    result = lq_start_num - lt_finish_num
    return result


def main():
    n, m = (int(x) for x in input().split())

    start_coords = []
    finish_coords = []
    for _ in range(n):
        a, b = (int(x) for x in input().split())
        start_coords.append(a)
        finish_coords.append(b)
    start_coords.sort()
    finish_coords.sort()

    assert len(start_coords) == len(finish_coords)

    points = [int(x) for x in input().split()]

    result = []
    for point in points:
        count = count_segments(point, start_coords, finish_coords, n)
        result.append(count)

    print(*result)


if __name__ == '__main__':
    main()
