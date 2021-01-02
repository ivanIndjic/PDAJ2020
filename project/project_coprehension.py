import math
from results import display_results, show_table
import tracemalloc
def GenerateMatrix(n, m):
    return [(j,i) for j in range(n) for i in range(m)]


def Calculate(m,n,coords):
    cordDict = {coords[i]: i for i in range(0,len(coords))}
    distanceMap={}
    finalList = []
    for point in GenerateMatrix(m,n):
        pointX,pointY = point
        distanceMap = dict((coord,nesto(coord,pointX,pointY)) for coord in coords)
        min_distance = min(distanceMap.items(), key=lambda x: x[1])
        finalList.append(cordDict.get(min_distance[0]))
    return finalList


def nesto (coord,pointX,pointY):
    x,y = coord.split(",")
    return math.sqrt((pointX-int(x))**2 + (pointY-int(y))**2)


def main():

    coords = ["1,3","3,2","6,8","9,6","5,5","12,12","66,3","13,2","6,38","9,16","5,35","52,2"]
    
    n = 1000
    m = 1000
    tracemalloc.start()
    res = Calculate(n,m,coords)
    #display_results(res,n,m,coords)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
    #show_table(res,n,m,coords)

if __name__ == "__main__":
    main()