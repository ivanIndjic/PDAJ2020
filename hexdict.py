import math

def generate(num=10):
    for i in range (num):
        yield i


def isPrime(num=10):
    numbers = generate(num)
    for i in numbers:
        for j in range(2,int(i)+1):
            if j == i:
                yield i
            if i % j == 0:
                break
            else:
                continue


def toHex(num):
    for i in isPrime(num):
        yield hex(i)


def createDict(num):
    diction = {}
    for i in toHex(num):
        xindex = str(i).find("x")
        rightside = str(i)[xindex+1:len(i)]
        for j in rightside:
            if j in diction:
                diction[j] += 1
            else:
                diction[j] = 1
    return diction
        
print(createDict(20))
