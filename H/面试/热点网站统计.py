import sys
def sortURL(lines, cache):
    n = int(lines.pop())
 
    for url in lines:
        cache[url] = cache.get(url, 0) + 1
 
    arr = []
    for key in cache:
        arr.append({
            "count": cache[key],
            "url": key
        })
 
    return ",".join([ele["url"] for ele in sorted(arr, key=lambda x: (-x["count"], x["url"]))[:n]]) 
lines = []
cache = {}
for line in sys.stdin:
    lines.append(line.strip())
 
    if line.strip().isdigit():
        print(sortURL(lines, cache))
        lines = []