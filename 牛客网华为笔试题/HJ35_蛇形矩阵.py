m = int(input())
# i，j是行和列，i从1到m, j是每行从1到m - i + 1，range右侧最大值不包括要加1 
# value=(i+j-2)*(i+j-1)/2+j
for i in range(1, m + 1):
    for j in range(1, m - i + 2):
        if j == m - i + 1:
            print((i + j - 2) * (i + j - 1) // 2 + j)
        else:
            # end默认是换行符所以print默认换行，但如果设定为' '，就是在后面加' '而不是换行了
            print((i + j - 2) * (i + j - 1) // 2 + j, end=' ')