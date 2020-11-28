
def generate(num=10):
    for i in range (num):
        yield i


def isPrime(num=10):
    for i in generate(num):
        for j in range(2,i+1):
            if j == i:
                print(i)
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
        rightside = str(i)[str(i).find("x")+1:len(i)]
        for j in rightside:
            diction[j]=diction[j]+1 if j in diction else 1

    return diction
        
print(createDict(20))
