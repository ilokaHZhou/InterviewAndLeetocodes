n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    tmp = arr[i]
    l = max(i * 100 - tmp, 0)
    r = tmp + i * 100
    arr[i] = [l, r]

start, end = arr[0]
res = []

for i in range(n):
    if arr[i][0] > end:
        res.append([start, end])
        start, end = arr[i]
    else:
        end = max(end, arr[i][1])

res.append([start, end])

start = res[0][1]
gap = 0

for i in range(1, len(res)):
    end = res[i][0]
    gap += end - start
    start = res[i][1]

print(gap)