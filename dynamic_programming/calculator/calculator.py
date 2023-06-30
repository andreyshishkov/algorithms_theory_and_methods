from typing import Tuple, List


def find_seq(n: int) -> Tuple[int, List[int]]:
    d = [0 for _ in range(n + 1)]
    seq = [n]
    for i in range(2, n + 1):
        x1 = d[i - 1]
        x2 = d[i // 2] if i % 2 == 0 else float('+inf')
        x3 = d[i // 3] if i % 3 == 0 else float('+inf')

        min_x = min(x1, x2, x3)
        d[i] = min_x + 1

    k = n
    while k > 1:
        if k % 3 == 0 and d[k] == (d[k // 3] + 1):
            k //= 3
        elif k % 2 == 0 and d[k] == (d[k // 2] + 1):
            k //= 2
        else:
            k -= 1
        seq.append(k)

    return d[n], seq[::-1]


def main():
    n = int(input())
    k, seq = find_seq(n)
    print(k)
    print(*seq)


if __name__ == '__main__':
    main()
