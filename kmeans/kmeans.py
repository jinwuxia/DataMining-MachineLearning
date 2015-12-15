import csv
import random


def loadDataset(filename, featureCount, dataset):
	with open(filename, "rb") as csvfile:
		lines = csv.reader(csvfile)
		dataset = list(lines)
		for x in range(len(dataset)):
			for y in range(featureCount)):
				dataset[x][y] = float(dataset[x][y])



def initChooseKCenter(dataset, K):
	centers=[]
	for i in range(K):
		index = random.randint(0, len(dataset)-1)
		centers.append(dataset[index])
	return centers

def euclideanDistance(instance1, insatnce2, length):
	sum = 0
	for index in range(length):
		sum += pow(instance1[index] - instance2[index], 2)
	return sqrt(sum)

def updateCenter(clusters):
	centers=[]
	
	for index in range(length(clusters)):
		eachCluster=clusters[index]
		for i in range(featureCount):
			sum(eachCluster)
			
	return centers



def kmeans(dataset, K):
	centers = initChooseKCenter(dataset,K)
	clusters=[] # clusters[0], clusters[1], ..., clusters[k]
	
	#init clusters	
	for i in range(k):
		clusters[i].append(centers[i])

	while ():
		for each in dataset:
			tmpdist=[]
			for i in range(K):
				dist = euclideanDistance(centers[i], each, featureCount)
				tmpdist.append(dist)
			# choose min in tmpdist, 
			minindex = tmpdist.index(min(tmpdist))
			clusters[minindex].append(each)
		
		# update centers
		centers = updateCenter(clusters)
				



def main():
	dataset=[]
	K = 4
	loadDataset(dataset)
	kmeans(dataset, K)







