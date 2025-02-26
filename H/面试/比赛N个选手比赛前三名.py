import sys

m, n = map(int, input().split(","))
scores = [list(map(int, input().split(","))) for _ in range(m)]
if m < 3 or m > 10 or n < 3 or n > 100:
    print("-1")
    sys.exit()
    
for i in range(m):
    for j in range(n):
        if scores[i][j] > 10 or scores[i][j] < 1:
            print("-1")
            sys.exit()
            
players = {}
            
for j in range(n):
    playerScores = [row[j] for row in scores]
    playerScores.sort(reverse=True)
    players[j] = playerScores
    
result = sorted(players.items(), key=lambda x: (sum(x[1]), x[1]), reverse=True)[:3]
result = [p[0]+1 for p in result]
result = ','.join(map(str, result))

print(result)