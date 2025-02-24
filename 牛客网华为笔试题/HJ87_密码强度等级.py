def password_strength(password):
    score = 0  # 初始化分数

    # 长度评分
    length = len(password)
    if length <= 4:
        score += 5
    elif 5 <= length <= 7:
        score += 10
    else:
        score += 25

    # 字母评分
    has_upper = any(c.isupper() for c in password)  # 是否有大写字母
    has_lower = any(c.islower() for c in password)  # 是否有小写字母
    if has_upper and has_lower:
        score += 20
    elif has_upper or has_lower:
        score += 10

    # 数字评分
    digit_count = sum(c.isdigit() for c in password)  # 数字个数
    if digit_count > 1:
        score += 20
    elif digit_count == 1:
        score += 10

    # 符号评分
    symbol_count = sum(not c.isalnum() for c in password)  # 符号个数
    if symbol_count > 1:
        score += 25
    elif symbol_count == 1:
        score += 10

    # 奖励评分
    if has_upper and has_lower and digit_count and symbol_count:
        score += 5
    elif (has_upper or has_lower) and digit_count and symbol_count:
        score += 3
    elif (has_upper or has_lower) and digit_count:
        score += 2

    # 根据总分确定强度等级
    if score >= 90:
        return "VERY_SECURE"
    elif score >= 80:
        return "SECURE"
    elif score >= 70:
        return "VERY_STRONG"
    elif score >= 60:
        return "STRONG"
    elif score >= 50:
        return "AVERAGE"
    elif score >= 25:
        return "WEAK"
    else:
        return "VERY_WEAK"


# 输入处理
password = input().strip()
print(password_strength(password))
