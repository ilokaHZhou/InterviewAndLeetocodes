import math

num_people, len_letter = map(int, input().split())
min_len_num = max(1, math.ceil(math.log10(num_people / pow(26, len_letter))))
print(min_len_num)