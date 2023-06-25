import heapq


def main():
    h = []
    heapq.heapify(h)

    n = int(input())
    for _ in range(n):
        operators = input().split()
        if operators[0] == 'Insert':
            value = -int(operators[1])
            heapq.heappush(h, value)
        else:
            value = heapq.heappop(h)
            print(-value)


if __name__ == '__main__':
    main()
