def calculate_distance(s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)

    d = [
        [i for i in range(m + 1)]
    ]

    for i in range(1, n + 1):
        d.append([i] + [0 for _ in range(1, m + 1)])

        for j in range(1, m + 1):
            d[1][j] = min(
                d[1][j - 1] + 1,
                d[0][j] + 1,
                d[0][j - 1] + (1 if s1[i - 1] != s2[j - 1] else 0)
            )

        del d[0]

    return d[0][-1]


def main():
    s1 = input()
    s2 = input()
    distance = calculate_distance(s1, s2)
    print(distance)


if __name__ == '__main__':
    main()
