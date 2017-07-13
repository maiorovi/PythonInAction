def isPermutationOfPalindrom(str):
    oddCount = 0
    dict = {}
    for ch in str:
        if ch.isalpha():
            if dict.__contains__(ch):
                dict[ch] += 1
            else:
                dict[ch] = 1
    for val in dict.values():
        if val % 2 != 0:
            oddCount += 1
    if (oddCount != 1):
        return False
    else:
        return True


print("tact coa is permutation: ", isPermutationOfPalindrom("tact coa"))
print("tact coa is permutation: ", isPermutationOfPalindrom("tact cqqa  "))