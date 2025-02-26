def main():
    # 处理输入
    money = int(input())
    topup_info = list(map(int, input().split()))

    dp = [0] * (money + 1)

    for i in range(len(topup_info)):
        for j in range(i + 1, money + 1):
            dp[j] = max(dp[j], dp[j - (i + 1)] + topup_info[i])

    print(dp[money])

if __name__ == "__main__":
    main()