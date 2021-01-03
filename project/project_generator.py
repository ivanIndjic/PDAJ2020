import math
from results import display_results, show_table
import tracemalloc
import time
cordDict = {}

def GenerateMatrix(n, m):
    for i in range(0,n):
        for j in range(0,m):
            yield (i,j)

def Calculate(m,n,coords):
    distanceMap = {}
    for point in GenerateMatrix(m,n):
        pointX,pointY = point
        for coord in coords: 
            distance = math.sqrt((pointX-coord[0])**2 + (pointY-coord[1])**2)
            distanceMap[coord] = distance
        min_distance = min(distanceMap.items(), key=lambda x: x[1])
        yield cordDict.get(min_distance[0])


def main():

    coords = ["11,300","9,420","1,3", "3,2", "6,8", "9,6", "5,5","15,15","76,54","89,430","336,423","211,211","350,350","426,18","0,500","7,420","766,894","999,3","876,542","667,718","319,54","1,800","803,20"]

    newcords = []
    n = 1000
    m = 1000
    tracemalloc.start()
    start_time = time.time()

    for i in range(0,len(coords)):
        x,y = coords[i].split(",")
        newcords.append((int(x),int(y)))
    for i in range(0,len(newcords)):
        cordDict[newcords[i]] = i
    res = Calculate(n,m,newcords)
    lista = list(res)
   # display_results(lista,n,m,coords)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    times = time.time() - start_time

    tracemalloc.stop()
    print(times)
   # show_table(lista,n,m,coords)

if __name__ == "__main__":
    main()