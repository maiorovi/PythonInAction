def compress(str):
    cur = str[0]
    count = 1
    res = ""
    for i in range(1, len(str), 1):
        if cur != str[i]:
            res += cur + count.__str__()
            cur = str[i]
            count = 1
        else:
            count += 1
    res +=  cur + count.__str__()
    return res


print(compress("aabcccccaaa"))
