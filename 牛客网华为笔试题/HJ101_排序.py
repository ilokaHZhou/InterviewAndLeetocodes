while True:
    try:
        n = input().strip()
        numbers = [int(num) for num in input().strip().split(' ')]
        ascending_order = int(input().strip()) == 0
        if ascending_order:
            # 因为是数字数组所以用这种print方式，否则需要把数组里每个元素转换为字符串
            print(*sorted(numbers), sep=' ')
        else:
            print(*sorted(numbers, reverse=True), sep=' ')
    except EOFError:
        break
