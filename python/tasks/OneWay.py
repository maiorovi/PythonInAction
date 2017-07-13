def one_way(str1, str2):
    if (abs(len(str1) - len(str2)) > 1):
        return False
    diffCounter = 0
    minLen = min(len(str1), len(str2))
    if len(str1) < len(str2):
        shorterStr = str1
        longerStr = str2
    else:
        shorterStr = str2
        longerStr = str1

    for ind in range(minLen):
        if diffCounter > 1:
            return False
        if shorterStr[ind] != longerStr[ind]:
            diffCounter += 1
            if ((ind+1) < minLen) and (shorterStr[ind+1] != longerStr[ind+1] and shorterStr[ind] != longerStr[ind+1]):
                diffCounter +=1

    return diffCounter < 2

print(one_way("pale", "ple")) #true
print(one_way("pales", "pale")) #true
print(one_way("pale", "bale")) #true
print(one_way("pale", "bake")) #false
print(one_way("paless", "pale")) #false
print(one_way("pale", "bald")) #false