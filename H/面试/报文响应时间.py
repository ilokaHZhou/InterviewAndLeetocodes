import sys

numQueries = int(input()) # 查询报文个数
arrivalTime = [0] * numQueries # HOST收到报文时间
maxRespCode = [0] * numQueries # 最大响应时间字段值

for i in range(numQueries):
    arrivalTime[i], maxRespCode[i] = map(int, input().split())

minResponseTime = sys.maxsize # HOST发送响应报文的时间
for i in range(numQueries):
    maxRespTime = 0
    if maxRespCode[i] < 128: # 当MaxRespCode < 128 ,MaxRespTime = MaxRespCode
        maxRespTime = maxRespCode[i]
    else: # 当MaxRespCode >= 128 ,MaxRespTime = (mant | 0x10) << (exp + 3)
        exp = (maxRespCode[i] & 0x70) >> 4 # exp 最大响应时间的 高5~7位
        mant = maxRespCode[i] & 0x0F # mant 为最大响应时间的 低4位
        maxRespTime = (mant | 0x10) << (exp + 3)
    responseTime = arrivalTime[i] + maxRespTime # HOST发送响应报文的时间
    minResponseTime = min(minResponseTime, responseTime) # 更新最小的 HOST发送响应报文的时间

print(minResponseTime)