L = int(input())
str = input()

def hash(str):
    inInt = []
    r = 31
    M = 1234567891
    for char in str:
        inInt.append(ord(char)-96)
    sum = 0
    for index, coeff in enumerate(inInt):
        sum += coeff * r**index
    hashVal = sum % M
    return hashVal

print(hash(str))