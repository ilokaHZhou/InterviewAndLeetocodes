n, k, x = map(int, input().split())
prices = list(map(int, input().split()))

sorted_prices = sorted(prices)
price_rating = sorted([(price, abs(price - x)) for price in sorted_prices], key=lambda item: item[1])
picked_price = sorted(item[0] for item in price_rating[:k])

print(' '.join(map(str, picked_price)))