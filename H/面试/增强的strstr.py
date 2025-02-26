import re

source = input()
target = input()

target = re.sub(r'\[(.*?)\]', r'[\1]', target)

pattern = re.compile(target)
matcher = pattern.search(source)

if matcher:
    print(matcher.start())
else:
    print(-1)