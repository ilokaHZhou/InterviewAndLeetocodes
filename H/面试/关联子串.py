import sys

def is_substring(str1, str2, start, len):
    count = 0
    freq = [0] * 26

    for i in range(len):
        freq[ord(str2[start + i]) - ord('a')] += 1

    for i in range(len):
        if freq[ord(str1[i]) - ord('a')] > 0:
            freq[ord(str1[i]) - ord('a')] -= 1
            count += 1

    return count == len

if __name__ == "__main__":
    strings = input().split(" ")
    str1 = strings[0]
    str2 = strings[1]
    n1 = len(str1)
    n2 = len(str2)
    index = -1

    for i in range(n2 - n1 + 1):
        if is_substring(str1, str2, i, n1):
            index = i
            break

    print(index)