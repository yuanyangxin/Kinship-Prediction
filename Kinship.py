import math
import matplotlib.pyplot as plt
import numpy as np
import random
from fileFinder import folderFind
from fileFinder import getCSV
from csvReader import csv_reader


rootdir = '/Users/quero/Desktop/ML/SemesterProject/FIDs_NEW'

def kinship(dir):

    kinList = [[],[]]
    
    for s in range(dir):
    
        csvFile = getCSV(rootdir, s)
        
        famList = csv_reader(csvFile)
        #in famList, fathers are indexed in 0 and sons in 1
        
        #print famList

        for rows in famList:
            
            imFather = folderFind(rootdir, s, rows[0])
            imSon = folderFind(rootdir, s, rows[1])
            
            if len(imFather) > 0 and len(imSon) > 0:
            
                if len(imFather) > len(imSon):
                
                    for i in range(len(imFather)-len(imSon)):
                        
                        imSon.append(imSon[0])
                
                elif len(imSon) > len(imFather):
                
                    for i in range(len(imSon)-len(imFather)):
                    
                        imFather.append(imFather[0])
                    
                kinList[0].append(imFather)
                kinList[1].append(imSon)
            
    #print len(kinList[1])
    #print len(kinList[0])
    dads = [val for sublist in kinList[0] for val in sublist] #Flatten lists
    sons = [val for sublist in kinList[1] for val in sublist] #Flatten lists
    print len(dads)
    #print len(sons)
    kinList = [[],[]] #Clear list to copy unidimentional list
    
    for n in range(len(dads)):
    
        kinList[0].append(dads[n])
        kinList[1].append(sons[n])
        
    return kinList
    
def unkinship(kinList):

    unkinList = [[],[]]
    
    randPair = 0

    for n in range(len(kinList[0])):
    
        while(randPair == n):
        
            randPair = random.randint(0,len(kinList[0])-1)
            
        unkinList[0].append(kinList[0][n])
        unkinList[1].append(kinList[1][randPair])

    return unkinList
    
def toSixChannels(List):

    dataset = []
    temp = np.empty((0,0,10000))

    for n in range(len(List[0])):

        temp = np.append(List[0][n], List[1][n], axis=2)
        
        dataset.append(temp)
                
    return dataset

def getDatasets(directory):

    #Returns ndarray of shape (no. of pictures, 224, 224, 6)
    #6 is the number of channels, 3 channels for each picture
    #data[0] is the list of related parents and sons
    #data[1] is the list of unrelated parents and sons

    kinList = kinship(directory)

    unkinList = unkinship(kinList)

    datasetKin = toSixChannels(kinList)
    datasetUnkin = toSixChannels(unkinList)
    
    return np.array(datasetKin), np.array(datasetUnkin)

data1, data2 = getDatasets(10)

print data1[0].shape

data1 = np.resize(data1,(len(data1),64,64,6))

print data1[[0]].shape



