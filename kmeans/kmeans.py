import csv
import random
import math
import os, sys

def loadDataset(filename, featureCount):
    dataset=[]
    with open(filename, "rb") as csvfile:
    	lines = csv.reader(csvfile)
    	dataset = list(lines)
    	for x in range(len(dataset)):
	    for y in range(featureCount):
    		dataset[x][y] = float(dataset[x][y])
    return dataset

# choose K center points randomly 
def initChooseKCenter(dataset, K):
    centers=[]
    for i in range(K):
    	index = random.randint(0, len(dataset)-1)
    	centers.append(dataset[index])
    return centers

def euclideanDistance(instance1, instance2, length):
    sum = 0
    for index in range(length):
    	sum += pow(instance1[index] - instance2[index], 2)
    return math.sqrt(sum)


def updateCenters(clustersDict, featureCount):
    K = len(clustersDict)
    centers=[]
    for i in range(K):
        eachCluster = list(clustersDict[i])
        center=[]
        length = len(eachCluster)
        for j in range(featureCount):
            tmp=0
            for i in range(length):
                tmp += eachCluster[i][j]
            center.append(tmp/float(length))
        centers.append(center)
    return centers

        
def updateClusters(centers, dataset, featureCount):
    K = len(centers)
    clusters=dict()
    for i in range(K):
        clusters[i] = list()
    
    classResult=[]
    for each in dataset:
    	tmpdist=[]
    	for i in range(K):
            dist = euclideanDistance(centers[i], each, featureCount)
	    tmpdist.append(dist)
	# choose min in tmpdist, 
	minindex = tmpdist.index(min(tmpdist))
	clusters[minindex].append(each)
        classResult.append(minindex)
    return clusters, classResult

def isNotStop(iterCount, oldCenters, centers, featureCount):
    MIN_ITER = 10000
    MIN_DIS = 0.001
    if(iterCount == 1):
        return True
    if(iterCount > MIN_ITER):
        return False
    for i in range(len(centers)):
        if euclideanDistance(centers[i], oldCenters[i], featureCount) > MIN_DIS:
            return True
    return False

def outputResult(dataset, classResult):
    for i in range(len(dataset)):
        print dataset[i], "   ", classResult[i]



def kmeans(dataset, K, featureCount):
    centers = initChooseKCenter(dataset,K)
    [clusters, classResult] = updateClusters(centers, dataset, featureCount)
    oldCenters = centers
    iterCount = 1
    while(isNotStop(iterCount, oldCenters, centers, featureCount)):
        centers = updateCenters(clusters, featureCount)
        [clusters, classResult] = updateClusters(centers, dataset, featureCount)
        iterCount+=1;

    outputResult(dataset, classResult)


def main():
    usage = "USAGE: python kmeans.py [FileName] [K] [FeatureCount]";
    if len(sys.argv) != 4:
        print "ERROR! ", usage;
        return 1
    filename = sys.argv[1]
    K = int(sys.argv[2])
    featureCount = int(sys.argv[3])

    dataset=[]
    dataset = loadDataset(filename, featureCount)
    kmeans(dataset, K, featureCount)


main()
