import math
from results import display_results, show_table
from multiprocessing import Pool
import tracemalloc

n,m = 5,5
def GenerateMatrix(coords):
    for i in range(n):
        for j in range(m):
            Calculate(i,j,coords)

def Calculate(m,n,coords):
    print(coords)
    cordDict = {}
    for i in range(0,len(coords)):
        cordDict[coords[i]] = i
    distanceMap = {}
    finalList = []
    pointX,pointY = m,n
    for coord in coords:
        x,y = coord.split(",")
        x,y = int(x),int(y)
        distance = math.sqrt((pointX-x)**2 + (pointY-y)**2)
        distanceMap[coord] = distance
        min_distance = min(distanceMap.items(), key=lambda x: x[1])
        return min_distance
        #finalList.append(cordDict.get(min_distance[0]))
    #print(finalList)
    #return finalList


def main():
    #coords = ["1,3","3,2","6,8","9,6","5,5", "11,11", "22,1", "13,8", "7,8", "9,9"]
    coords = ["1,2", "3,1"]
    n = 5
    m = 5
    tracemalloc.start()
    with Pool(4) as pool:
        r = pool.imap(GenerateMatrix, coords)
        for i in r:
            if i is not None:
                print(r)
    res = Calculate(n,m,coords)
    #display_results(res,n,m,coords)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
    #show_table(res,n,m,coords)

if __name__ == "__main__":
    main()