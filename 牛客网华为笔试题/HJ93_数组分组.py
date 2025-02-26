def add(sm5,sm3,temp):
    if len(temp)==0:
        if sm5==sm3:
            return True
        else:
            return False
    else:
        return add(sm5+temp[0],sm3,temp[1:]) or add(sm5,sm3+temp[0],temp[1:])
while True:
    try:
        n=int(input())
        nums=list(map(int,input().split()))
        num3=[]
        num5=[]
        temp=[]
        for i in nums:
            if i%5==0:
                num5.append(i)
            elif i%3==0:
                num3.append(i)
            else:
                temp.append(i)
        sm5,sm3=sum(num5),sum(num3)
        a=add(sm5,sm3,temp)
        if a:
            print('true')
        else:
            print('false')
    except:
        break