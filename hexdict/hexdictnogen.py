import tracemalloc
def generate(num=10):
    return [i for i in range(num)]


def isPrime(num=10):
    numbers = []
    for i in generate(num):
        for j in range(2,i+1):
            if j == i:
                numbers.append(i)
            if i % j == 0:
                break
            else:
                continue
    return numbers


def toHex(num):
    return [hex(i) for i in range(num)]


def createDict(num):
    diction = {}
    numb = toHex(num)
    for i in numb:
        rightside = str(i)[str(i).find("x")+1:len(str(i))]
        for j in rightside:
            diction[j]=diction[j]+1 if j in diction else 1

    return diction
        

def main():
    tracemalloc.start()
    print(createDict(50000))
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()

if __name__ == "__main__":
    main()