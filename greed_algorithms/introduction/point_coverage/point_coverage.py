n = int(input())
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
k = 0
arr = sorted(arr, key=lambda x: x[1])
arr_of_keys = []
arr_of_keys.append(arr[0][1])
l = arr[0][1]
for i in range(1, len(arr)):
    if l < arr[i][0]:
        k += 1
        l = arr[i][1]
        arr_of_keys.append(l)

print(k + 1)
print(' '.join([str(i) for i in arr_of_keys]))
