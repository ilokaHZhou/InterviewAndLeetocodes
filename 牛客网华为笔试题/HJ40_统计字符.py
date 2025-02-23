def count_characters(s):
    letter_count = 0
    digit_count = 0
    space_count = 0
    other_count = 0

    for char in s:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1
        else:
            other_count += 1

    return letter_count, digit_count, space_count, other_count

s = input()
letter, digit, space, other = count_characters(s)
print(letter)
print(space)
print(digit)
print(other)