def isStringUnique(str):
    container = set()
    for i in str:
        if (not container.__contains__(i)):
            container.add(i)
        else:
            return False
    return True

print("Hello World is unique: " + isStringUnique("Hello World").__str__())
print("abc is unique: " + isStringUnique("abc").__str__())