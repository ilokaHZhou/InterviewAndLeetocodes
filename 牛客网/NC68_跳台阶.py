"""
假设有n阶台阶，在所有的跳法中，由于青蛙一次只能跳1步或者2步，所以青蛙跳上最后一阶只能由f(n-1)+1 或者f(n-2)+2 这两种情况得来。
即：f(n)=f(n-1)+f(n-2)
同理:f(n-1)=f(n-2)+f(n-3),以此类推。
这其实就是一个斐波拉契数列。
"""
class Solution:
    def jumpFloor(self , number: int) -> int:
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        
        prev, curr = 1, 2
        for _ in range(3, number + 1):
            prev, curr = curr, prev + curr
        return curr