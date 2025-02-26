n, d = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

pairs = [0] * (n+1)
min_sum = [0] * (n+1)

for i in range(2, n+1):
    tmp = 0
    if nums[i-1] - nums[i-2] <= d:
        tmp += 1
    if pairs[i-2] + tmp > pairs[i-1]:
        pairs[i] = pairs[i-2] + tmp
        min_sum[i] = min_sum[i-2] + nums[i-1] - nums[i-2]
    elif pairs[i-2] + tmp < pairs[i-1]:
        pairs[i] = pairs[i-1]
        min_sum[i] = min_sum[i-1]
    else:
        if tmp == 1:
            min_sum[i] = min(min_sum[i-1], min_sum[i-2] + nums[i-1] - nums[i-2])
        else:
            min_sum[i] = min(min_sum[i-1], min_sum[i-2])
        pairs[i] = pairs[i-1]

if pairs[n] == 0:
    print(-1)
else:
    print(min_sum[n])