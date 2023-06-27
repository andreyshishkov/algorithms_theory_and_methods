def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    result = arr.copy()
    b = [0] * 11

    for a in arr:
        b[a] += 1

    for i in range(1, 11):
        b[i] = b[i] + b[i - 1]

    for i in range(n - 1, -1, -1):
        result[b[arr[i]] - 1] = arr[i]
        b[arr[i]] -= 1

    print(*result)


if __name__ == '__main__':
    main()
