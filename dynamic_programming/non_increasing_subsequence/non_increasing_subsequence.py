from typing import List, Tuple


def get_ceil_index(arr: List[int], tmp: List[int], left: int, right: int, key: int) -> int:
    while right - left > 1:
        middle = (left + right) // 2
        if arr[tmp[middle]] > key:
            right = middle
        else:
            left = middle

    return right


def count_subseq(arr: List[int], n: int) -> Tuple[List[int], int]:
    tail_indices = [0 for _ in range(n + 1)]
    prev_indices = [-1 for _ in range(n + 1)]

    length = 1
    for i in range(1, n):

        if arr[i] < arr[tail_indices[0]]:

            tail_indices[0] = i

        elif arr[i] >= arr[tail_indices[length - 1]]:
            prev_indices[i] = tail_indices[length - 1]
            tail_indices[length] = i
            length += 1

        else:
            pos = get_ceil_index(arr, tail_indices, -1, length - 1, arr[i])
            prev_indices[i] = tail_indices[pos - 1]
            tail_indices[pos] = i

    i = tail_indices[length - 1]
    lis = []
    while i >= 0:
        lis.append(i + 1)
        i = prev_indices[i]
    return lis[::-1], length


def main():
    n = int(input())
    arr = [-int(x) for x in input().split()]
    seq, length = count_subseq(arr, n)
    print(length)
    print(*seq)


if __name__ == '__main__':
    main()
