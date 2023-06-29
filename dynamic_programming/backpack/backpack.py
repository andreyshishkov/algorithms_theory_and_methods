from typing import List


def get_max_weight(weights: List[int], capacity: int, n: int) -> int:
    d = [
        [0 for _ in range(n + 1)] for _ in range(capacity + 1)
    ]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            d[w][i] = d[w][i - 1]
            if weights[i - 1] <= w:
                d[w][i] = max(
                    d[w][i],
                    d[w - weights[i - 1]][i - 1] + weights[i - 1]
                )
    return d[capacity][n]


def main():
    capacity, n = (int(x) for x in input().split())
    weights = [int(x) for x in input().split()]

    result = get_max_weight(weights, capacity, n)
    print(result)


if __name__ == '__main__':
    main()
