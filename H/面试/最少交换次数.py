nums = list(map(int, input().split()))
k = int(input())

count = sum(1 for num in nums if num < k)
if count == 1:
    print(0)
    exit()

min_swap_count = sum(1 for num in nums[:count] if num >= k)
tmp_swap_count = min_swap_count

for j in range(count, len(nums)):
    pre_left = j - count
    cur_right = j
    if nums[pre_left] >= k and nums[cur_right] < k:
        tmp_swap_count -= 1
    elif nums[pre_left] < k and nums[cur_right] >= k:
        tmp_swap_count += 1
    min_swap_count = min(min_swap_count, tmp_swap_count)

print(min_swap_count)