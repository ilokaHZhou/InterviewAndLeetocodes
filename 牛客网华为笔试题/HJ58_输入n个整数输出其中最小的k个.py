n, k = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))
result = sorted(numbers)[:k]
print(*result, sep=' ')