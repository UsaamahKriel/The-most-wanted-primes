import math


def isPrime(n): # the function that check whether or not a number is prime
    for i in range(2, int(math.sqrt(n)+1)): # the +1 prevents it from mistaking a square number as a prime number
        if (n % i == 0):
            return False
    return True


def findPalindromePrime():
    startNum = 11
    num = ""
    flag = True
    while flag:  # palindrome prime
        for j in range(1, startNum + 1):
            num += str(j)
        for j in range(startNum - 1, 0, -1):
            num += str(j)
        if isPrime((int(num))):
            flag = False
            return num
        startNum += 1
        num = ""


def findUniquePrime():
    flag = True
    startNum = 123

    while flag:
        if isPrime(startNum):
            flag = False
        else:
            startNum = int(str(startNum) + str(int(str(startNum)[len(str(startNum)) - 1]) + 1))
    return startNum


def findMostWantedPrime():
    startNum = 123
    j = 3
    while flag:
        if isPrime(startNum):
            flag = False
            print(startNum, "hi")
        else:
            startNum = int(str(startNum) + str(j + 1))
        j += 1
    return startNum
