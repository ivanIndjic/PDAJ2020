import math
from results import display_results, show_table
import tracemalloc
import time
def GenerateMatrix(n, m):
    return [(j,i) for j in range(n) for i in range(m)]


def Calculate(m,n,coords):
    cordDict = {coords[i]: i for i in range(0,len(coords))}
    distanceMap={}
    finalList = []
    for point in GenerateMatrix(m,n):
        pointX,pointY = point
        distanceMap = dict((coord,transform(coord,pointX,pointY)) for coord in coords)
        min_distance = min(distanceMap.items(), key=lambda x: x[1])
        finalList.append(cordDict.get(min_distance[0]))
    return finalList


def transform (coord,pointX,pointY):
    x,y = coord.split(",")
    return math.sqrt((pointX-int(x))**2 + (pointY-int(y))**2)


def main():

    coords = ["11,300","9,420","1,3", "3,2", "6,8", "9,6", "5,5","15,15","76,54","89,430","336,423","211,211","350,350","426,18","0,500","7,420","766,894","999,3","876,542","667,718","319,54","1,800","803,20"]
    
    n = 1000
    m = 1000
    tracemalloc.start()
    start_time = time.time()

    res = Calculate(n,m,coords)
    #display_results(res,n,m,coords)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
    times = time.time() - start_time
    print(times)
    #show_table(res,n,m,coords)

if __name__ == "__main__":
    main()