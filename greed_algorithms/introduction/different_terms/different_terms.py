n = int(input())
arr = []
for i in range(1, n+1):
    if (n - i) >= (i + 1):
        arr.append(i)
        n -= i
    else:
        arr.append(n)
        break
print(len(arr))
print(*arr)
