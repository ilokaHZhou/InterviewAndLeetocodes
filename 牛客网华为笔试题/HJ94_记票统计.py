def count_votes(candidates, votes):
    candidate_count = {candidate: 0 for candidate in candidates}  # 初始化候选人票数
    invalid = 0  # 无效票数

    for vote in votes:  # 遍历选票
        if vote in candidate_count:  # 如果选票有效
            candidate_count[vote] += 1  # 对应候选人票数加 1
        else:  # 如果选票无效
            invalid += 1  # 无效票数加 1

    # 输出结果
    for candidate in candidates:
        print(f"{candidate} : {candidate_count[candidate]}")
    print(f"Invalid : {invalid}")


# 输入处理
n = int(input())  # 候选人人数
candidates = input().split()  # 候选人名单
m = int(input())  # 投票人数
votes = input().split()  # 投票结果

# 调用函数
count_votes(candidates, votes)
