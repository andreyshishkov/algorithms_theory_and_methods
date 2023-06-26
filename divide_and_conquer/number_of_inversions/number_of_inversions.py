from typing import List


def merge(arr: List[int], tmp: List[int], low: int, mid: int, high: int) -> int:
    k = i = low
    j = mid + 1
    inversion_count = 0

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
            inversion_count += (mid - i + 1)

        k += 1

    while i <= mid:
        tmp[k] = arr[i]
        k += 1
        i += 1

    for i in range(low, high + 1):
        arr[i] = tmp[i]

    return inversion_count


def merge_sort(arr: List[int], tmp: List[int], low: int, high: int) -> int:
    if high <= low:
        return 0

    mid = (low + high) // 2
    inversion_count = 0

    inversion_count += merge_sort(arr, tmp, low, mid)
    inversion_count += merge_sort(arr, tmp, mid + 1, high)
    inversion_count += merge(arr, tmp, low, mid, high)

    return inversion_count


def count_inversions(arr: List[int]) -> int:
    tmp = arr.copy()
    inversion_count = merge_sort(arr, tmp, 0, len(arr) - 1)
    return inversion_count


def main():
    _ = int(input())
    arr = [int(x) for x in input().split()]
    result = count_inversions(arr)
    print(result)


if __name__ == '__main__':
    main()
