temp = input()
while(len(temp)>0):
    # temp[:8]是从头数8个，ljust用来左对齐，参数用来填充，temp[8:]是跳过8个字符往后找
    print(temp[:8].ljust(8,"0"))
    temp = temp[8:]