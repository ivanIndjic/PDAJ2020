from django.shortcuts import render
from rest_framework.views import APIView
import json
import time
import math
import tracemalloc
from django.http import HttpResponse
from multiprocessing import Pool

cordDict = {}

# Create your views here.
####################Generators###############################3
def GenerateMatrixGenerator(n, m):
    for i in range(0,n):
        for j in range(0,m):
            yield (i,j)

def CalculateGenerator(n,m,coords):
    distanceMap = {}
    for point in GenerateMatrixGenerator(m,n):
        pointX,pointY = point
        for coord in coords: 
            distance = math.sqrt((pointX-coord[0])**2 + (pointY-coord[1])**2)
            distanceMap[coord] = distance
        min_distance = min(distanceMap.items(), key=lambda x: x[1])
        yield cordDict.get(min_distance[0])

def CreateJson(m,n,coords):
    results = []
    for i in CalculateGenerator(m,n,coords):
        results.append(i)
    json_response = {
        "result": results
    }
    return json_response
#######################################################################

###############################Parallel################################
def GenerateMatrixParallel(coords, n, m):
    for i in range(0,n):
        for j in range(0,m):
            yield (coords,(i,j))

def CalculateParallel(args):
    coords, point = args
    distanceMap = {}
    pointX,pointY = point
    for coord in coords:
        distance = math.sqrt((pointX-coord[0])**2 + (pointY-coord[1])**2)
        distanceMap[coord] = distance
    return cordDict.get(min(distanceMap.items(), key=lambda x: x[1])[0])
#######################################################################

###############################Sequential##############################
def GenerateMatrixSeq(n, m):
    matrix = []
    for i in range(n):
        for j in range(m):
            matrix.append((i,j))
    return matrix

def Calculate(n,m,coords,cordDict):
    distanceMap = {}
    finalList = []
    for point in GenerateMatrixSeq(n,m):
        pointX,pointY = point
        for coord in coords:
            distance = math.sqrt((pointX-coord[0])**2 + (pointY-coord[1])**2)
            distanceMap[coord] = distance
        min_distance = min(distanceMap.items(), key=lambda x: x[1])
        finalList.append(cordDict.get(min_distance[0]))
    json_response = {
        "result": finalList
    }
    return json_response
########################################################################

##########################List Comprehension############################
def GenerateMatrixComprehension(n, m):
    return [(j,i) for j in range(n) for i in range(m)]


def CalculateComprehension(m,n,coords):
    cordDict = {coords[i]: i for i in range(0,len(coords))}
    distanceMap = {}
    finalList = []
    for point in GenerateMatrixComprehension(m,n):
        pointX,pointY = point
        for coord in coords:
            x,y = coord.split(",")
            x,y = int(x),int(y)
            distance = math.sqrt((pointX-x)**2 + (pointY-y)**2)
            distanceMap[coord] = distance
        min_distance = min(distanceMap.items(), key=lambda x: x[1])
        finalList.append(cordDict.get(min_distance[0]))
    json_response = {
        "result": finalList
    }
    return json_response
########################################################################
class SeqCalculationsAPI(APIView):
    def post(self,request):
        return SeqMain(request)

def SeqMain(request):
    cordDict = {}
    newcords = []
    tracemalloc.start()
    start_time = time.time()
    for i in range(0,len(request.data["points"])):
        x,y = request.data["points"][i].split(",")
        newcords.append((int(x),int(y)))
    for i in range(0,len(newcords)):
        cordDict[newcords[i]] = i
    results = Calculate(request.data["n"], request.data["m"], newcords,cordDict)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    results["time_in_s"] = time.time() - start_time
    results["max_memory_in_MB"] = peak / 10**6
    dump = json.dumps(results)
    cordDict = {}
    return HttpResponse(dump,content_type='application/json')


class CompCalculationsAPI(APIView):
    def post(self,request):
        return CompMain(request)

def CompMain(request):
    tracemalloc.start()
    start_time = time.time()
    results = CalculateComprehension(request.data["n"], request.data["m"], request.data["points"])
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    results["time_in_s"] = time.time() - start_time
    results["max_memory_in_MB"] = peak / 10**6
    dump = json.dumps(results)
    return HttpResponse(dump,content_type='application/json')

class GenCalculationsAPI(APIView):
    def post(self,request):
        return MainGen(request)

def MainGen(request):
    newcords = []
    cordDict = {}
    tracemalloc.start()
    start_time = time.time()
    for i in range(0,len(request.data["points"])):
        x,y = request.data["points"][i].split(",")
        newcords.append((int(x),int(y)))
    for i in range(0,len(newcords)):
        cordDict[newcords[i]] = i
    results = CreateJson(request.data["n"], request.data["m"], newcords)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    results["time_in_s"] = time.time() - start_time
    results["max_memory_in_MB"] = peak / 10**6
    cordDict = {}
    dump = json.dumps(results)
    return HttpResponse(dump,content_type='application/json')


class ParCalculationsAPI(APIView):
    def post(self, request):
        return ParMain(request)

def ParMain(request):
    cordDict = {}
    newcords = []
    results = []
    tracemalloc.start()
    start_time = time.time()
    for i in range(0,len(request.data["points"])):
        x,y = request.data["points"][i].split(",")
        newcords.append((int(x),int(y)))
    for i in range(0,len(newcords)):
        cordDict[newcords[i]] = i
    with Pool(4) as pool:
        r = pool.imap(CalculateParallel, GenerateMatrixParallel(newcords, request.data["n"], request.data["m"]),chunksize=request.data["n"])
        results = list(r)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    json_response = {
        "result": results
    }
    json_response["time_in_s"] = time.time() - start_time
    json_response["max_memory_in_MB"] = peak / 10**6
    dump = json.dumps(json_response)
    cordDict = {}
    return HttpResponse(dump,content_type='application/json')
'''
def MainSeq(request):
    cordDict = {}
    newcords = []
    tracemalloc.start()
    start_time = time.time()
    for i in range(0,len(request.data["points"])):
        x,y = request.data["points"][i].split(",")
        newcords.append((int(x),int(y)))
    for i in range(0,len(newcords)):
        cordDict[newcords[i]] = i
    results = Calculate(request.data["n"], request.data["m"], newcords,cordDict)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    results["time_in_s"] = time.time() - start_time
    results["max_memory_in_MB"] = peak / 10**6
    dump = json.dumps(results)
    cordDict = {}
    return HttpResponse(dump,content_type='application/json')
def MainGenerator(request):
    newcords = []
    cordDict = {}
    tracemalloc.start()
    start_time = time.time()
    for i in range(0,len(request.data["points"])):
        x,y = request.data["points"][i].split(",")
        newcords.append((int(x),int(y)))
    for i in range(0,len(newcords)):
        cordDict[newcords[i]] = i
    results = CreateJson(request.data["n"], request.data["m"], newcords)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    results["time_in_s"] = time.time() - start_time
    results["max_memory_in_MB"] = peak / 10**6
    cordDict = {}
    dump = json.dumps(results)
    return HttpResponse(dump,content_type='application/json')

def MainParallel(request):
    cordDict = {}
    newcords = []
    results = []
    tracemalloc.start()
    start_time = time.time()
    for i in range(0,len(request.data["points"])):
        x,y = request.data["points"][i].split(",")
        newcords.append((int(x),int(y)))
    for i in range(0,len(newcords)):
        cordDict[newcords[i]] = i
    with Pool(4) as pool:
        r = pool.imap(CalculateParallel, GenerateMatrixParallel(newcords, request.data["n"], request.data["m"]),chunksize=request.data["n"])
        results = list(r)
    #results = CreateJson(request.data["n"], request.data["m"], newcords)
    json_response = {
        "result": results
    }
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    json_response["time_in_s"] = time.time() - start_time
    json_response["max_memory_in_MB"] = peak / 10**6
    dump = json.dumps(json_response)
    cordDict = {}
    return HttpResponse(dump,content_type='application/json')
def MainComprehension(request):
    tracemalloc.start()
    start_time = time.time()
    results = CalculateComprehension(request.data["n"], request.data["m"], request.data["points"])
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    results["time_in_s"] = time.time() - start_time
    results["max_memory_in_MB"] = peak / 10**6
    dump = json.dumps(results)
    return HttpResponse(dump,content_type='application/json')
    '''