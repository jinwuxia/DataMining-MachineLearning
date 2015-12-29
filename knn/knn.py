"""
This is a complete python program whose function is KNN.
KNN, K-nearest Neighbours,  is one of the most common classfication algorithms in machine learning.
This program comes from:
	 http://machinelearningmastery.com/tutorial-to-implement-k-nearest-neighbors-in-python-from-scratch/ 


function: automatic divide data into trainning set and test set;
          output classification result and accuracy
USAGE:
     python knn.py [datafile.csv]  [K-knn argv]  [featureCount]

"""

import csv
import random 
import math
import operator
import os, sys

def loadDataset(filename, featureCount, split,trainingSet=[], testSet=[]):
	with open(filename, 'rb') as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range(len(dataset)-1):
			for y in range(featureCount):
				dataset[x][y] = float(dataset[x][y])
			if random.random() < split:
				trainingSet.append(dataset[x])
			else:
				testSet.append(dataset[x])



def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
                #print instance1, "   ",instance2
		distance += pow(instance2[x]-instance1[x], 2)
	distance = math.sqrt(distance)
	return distance

def getKNeighbors(trainingSet, testInstance, k):
	distances=[]
	featureCount = len(testInstance)-1
	for  x in range(len(trainingSet)):
		dist = euclideanDistance(trainingSet[x], testInstance, featureCount)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors=[]
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors	


def getResponse(neighbors):
	classVotes={}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse= True)
	return sortedVotes[0][0]


def getAccuracy(testSet, prediction):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == prediction[x]:
			correct+=1
	return correct/float(len(testSet)) * 100


def main():
        usage = "USAGE: python knn.py datafile.csv K[knn argv] featureCount"
        if len(sys.argv) != 4:
            print "Error parameter!  ", usage
            return 1
        datafile = sys.argv[1]
        k = int(sys.argv[2])
        feature = int(sys.argv[3])

        trainingSet = []
	testSet= []
	predictions = []
	split= 0.66
	loadDataset(datafile, feature, split, trainingSet, testSet)
	print 'Train: ' + repr(len(trainingSet))
	print 'Test: ' + repr(len(testSet))
	
	k = 3
	for x in range(len(testSet)):
		neighbors = getKNeighbors(trainingSet, testSet[x], k)
		response = getResponse(neighbors)
		print 'predicted =', response, ',  actual=', testSet[x][-1]
		predictions.append(response)
	accuracy = getAccuracy(testSet, predictions)
	print "Accuracy: ", accuracy

main()
