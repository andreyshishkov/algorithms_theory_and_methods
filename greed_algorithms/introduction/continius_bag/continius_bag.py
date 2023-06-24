def max_ind(arr):
    max_ind = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_ind]:
            max_ind = i
    return max_ind

n, volum = list(map(int, input().split()))
arr = []
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
arr_x = [i[0]/i[1] for i in arr]
k = 0
while volum > 0 and len(arr_x) > 0:
    m = max_ind(arr_x)
    if volum >= arr[m][1]:
        k += arr[m][0]
        volum -= arr[m][1]
    else:
        k += arr[m][0] * volum/arr[m][1]
        volum = 0
    del arr_x[m]
    del arr[m]
print(round(k, 3))
