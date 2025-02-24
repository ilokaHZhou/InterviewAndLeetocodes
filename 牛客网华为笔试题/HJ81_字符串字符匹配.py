s = input().strip()
t = input().strip()
result = 'true'
for c in s:
    if c not in t:
        result = 'false'
print(result)