def encrypt(s):
    result = []
    for char in s:
        if char.isalpha():
            if char == 'z':
                result.append('A')
            elif char == 'Z':
                result.append('a')
            else:
                result.append(chr(ord(char) + 1).swapcase())
        elif char.isdigit():
            result.append(str((int(char) + 1) % 10))
        else:
            result.append(char)
    return ''.join(result)

def decrypt(s):
    result = []
    for char in s:
        if char.isalpha():
            if char == 'A':
                result.append('z')
            elif char == 'a':
                result.append('Z')
            else:
                result.append(chr(ord(char) - 1).swapcase())
        elif char.isdigit():
            result.append(str((int(char) - 1) % 10))
        else:
            result.append(char)
    return ''.join(result)

# 读取输入
print(encrypt(input().strip()))
print(decrypt(input().strip()))
