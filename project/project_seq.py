import math
from results import display_results, show_table
import tracemalloc
import time
cordDict = {}

def GenerateMatrix(n, m):
    matrix = []
    for i in range(n):
        for j in range(m):
            matrix.append((i,j))
    return matrix

def Calculate(m,n,coords):
    distanceMap = {}
    finalList = []
    for point in GenerateMatrix(m,n):
        pointX,pointY = point
        for coord in coords:
            distance = math.sqrt((pointX-coord[0])**2 + (pointY-coord[1])**2)
            distanceMap[coord] = distance
        min_distance = min(distanceMap.items(), key=lambda x: x[1])
        finalList.append(cordDict.get(min_distance[0]))
    return finalList


def main():
    newcords = []
    coords = ["11,110","19,420","11,3", "3,21", "6,8", "9,16", "5,5","15,15","76,54","89,430","331,423","211,211","350,350","426,18","0,500","7,420","766,894","999,3","876,542","667,718","319,54","1,800","803,20"]


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
  #  display_results(res,n,m,coords)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    times = time.time() - start_time

    tracemalloc.stop()
    print(times)
   # show_table(res,n,m,coords)

if __name__ == "__main__":
    main()