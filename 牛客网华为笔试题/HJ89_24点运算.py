a = input().split(' ')
dictory = {'J':11,'Q':12,'K':13,'A':1}
def dfs(wait,target,out):
    if len(wait) == 1:
        if wait[0] in dictory:
            c = dictory[wait[0]]
        else:
            c = int(wait[0])
        if target == c:
            L.append(wait[0]+out)
    else:
        for i in range(len(wait)):
            w = wait[:i]+wait[i+1::]
            if wait[i] in dictory:
                c = dictory[wait[i]]
            else:
                c = int(wait[i])
            dfs(w,target-c,'+'+wait[i]+out)
            dfs(w,target+c,'-'+wait[i]+out)
            dfs(w,target*c,'/'+wait[i]+out)
            dfs(w,target/c,'*'+wait[i]+out)
 
L = []
if 'joker' in a or 'JOKER' in a:
    print('ERROR')
else:
    dfs(a,24,'')
    if not L:
        print('NONE')
    else:
        print(L[0])