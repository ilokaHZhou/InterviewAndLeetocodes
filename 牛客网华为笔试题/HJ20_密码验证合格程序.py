import sys


def is_valid_password(password):
    # 条件1：长度超过8位
    if len(password) <= 8:
        return False

    # 条件2：必须包含大写字母、小写字母、数字、特殊字符中的至少三种
    categories = 0
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    categories = sum([has_upper, has_lower, has_digit, has_special])
    if categories < 3:
        return False

    # 条件3：不能有长度大于2的重复子串
    for i in range(len(password) - 3):
        substr = password[i : i + 3]
        if substr in password[i + 3 :]:
            return False

    return True


# 测试
for line in sys.stdin:
    password = line.strip()
    if is_valid_password(password):
        print("OK")
    else:
        print("NG")
