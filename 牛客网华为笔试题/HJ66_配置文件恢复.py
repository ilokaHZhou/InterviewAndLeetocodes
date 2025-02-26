while True:
    try:
        m=input().strip().split()
        key=["reset","reset board","board add","board delete","reboot backplane","backplane abort"]
        value=["reset what","board fault","where to add","no board at all","impossible","install first"]
        #不建字典，用列表的方式避免了双层循环，如果实在要用列表，直接用dict(zip（list1,list2）)合成字典都行.
        if len(m)<1 or len(m)>2:   #判断当输入为小于1个或者输入大于2个字符串时，不符合命令，就报未知命令
            print("unknown command")
        elif len(m)==1:   #当输入一个字符串
            if m[0]==key[0][:len(m[0])]:  #这里才是解决这个题的最佳思想，利用切片的思想来匹配
                print(value[0])
            else:
                print("unknown command")
        else:
            index=[]
            for i in range(1,len(key)): #这里把所有原始命令遍历，如果这里写成(len(key)+1),也就是1..6，那么下面的key[i]要改成k[i-1]才符合逻辑
                a=key[i].split() #将具体的一个KEY分割成两部分
                if m[0]==a[0][:len(m[0])] and m[1]==a[1][:len(m[1])]:  #然后去匹配被分割的key,这里不可能有reset这种单独的，因为上面条件已经限制了。
                    index.append(i)  #符合条件就把这个位置入列表
            if len(index)!=1:
                print("unknown command")
            else:
                print(value[index[0]]) #输出对应的value值
    except:
        break