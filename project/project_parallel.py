import math
from results import display_results, show_table
import tracemalloc
from multiprocessing import Pool
import time

cordDict = {}

def GenerateMatrix(coords, n, m):
    for i in range(0,n):
        for j in range(0,m):
            yield (coords,(i,j))

def Calculate(args):
    coords, point = args
    distanceMap = {}
    pointX,pointY = point
    for coord in coords:
        distance = math.sqrt((pointX-coord[0])**2 + (pointY-coord[1])**2)
        distanceMap[coord] = distance
    return cordDict.get(min(distanceMap.items(), key=lambda x: x[1])[0])


def main():
    #coords = ["4,3","3,4","6,8","9,6","4,5","12,11","66,3","13,2","6,38","9,16","5,35","52,2"]
 #   coords = ["1,2", "3,1","6,8","9,6","5,5"]
    newcords = []
    n = 1000
    m = 1000
    coords = ["11,300","9,420","1,3", "3,2", "6,8", "9,6", "5,5","15,15","76,54","89,430","336,423","211,211","350,350","426,18","0,500","7,420","766,894","999,3","876,542","667,718","319,54","1,800","803,20"]
    for i in range(0,len(coords)):
        x,y = coords[i].split(",")
        newcords.append((int(x),int(y)))
    for i in range(0,len(newcords)):
        cordDict[newcords[i]] = i
    
    tracemalloc.start()
    start_time = time.time()
    with Pool(4) as pool:
        r = pool.imap_unordered(Calculate, GenerateMatrix(newcords, n, m),chunksize=n)
        res = list(r)
    #    display_results(res,n,m,coords)
   #     show_table(res,n,m,coords)
    current, peak = tracemalloc.get_traced_memory()
    times = time.time() - start_time
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    print(times)
    tracemalloc.stop()

if __name__ == "__main__":
    main()