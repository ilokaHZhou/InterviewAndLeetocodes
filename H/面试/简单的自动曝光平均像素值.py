import sys
input_str = sys.stdin.readline().strip()
img = list(map(int, input_str.split()))
len = len(img)
min_diff = sys.maxsize
k_ans = 0

for k in range(-127, 129):
    sum = 0
    for i in range(len):
        new_val = img[i] + k
        new_val = max(0, min(new_val, 255))
        sum += new_val
    diff = abs(sum / len - 128)
    if diff < min_diff:
        min_diff = diff
        k_ans = k
    elif diff == min_diff and k_ans != 0:
        k_ans = min(k_ans, k)

print(k_ans)