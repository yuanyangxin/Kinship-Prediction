import csv
import operator
import numpy as np
import copy

#The purpose of this code is to take a csv of the kinship DB and return a dictionary containing all male fathers and their sons.

def csv_reader(file_obj):

    reader = csv.reader(file_obj)
    fam_matrix = []
    for row in reader:
        #print(" ".join(row))
        fam_matrix.append(row)
        
    fam_matrix_Index = getMales(fam_matrix)
    
    fam_matrix = fam_matrix[1:]
    
    fam_matrix = removeFemales(fam_matrix, fam_matrix_Index)
    
    FatherSonList = getFatherSonList(fam_matrix)
    
    return FatherSonList

def getMales(matrix):

    length = 0
    n = 0
    genders = []
    males = []

    for s in matrix[0]:
    
    #This loop counts how many familiy members there are into the variable length

        for t in s.split():
        
            if t.isdigit():
            
                length += 1
                
    
    for rows in matrix:
    
    #This loop gets the genders from the gender column and appends it into an array called genders
                
      genders.append( matrix[n][length+1])

      n+=1

    genders = genders[1:]
    
    for s in genders:
    
    #This loop creates a binary array called males with male members set to 1
    
        if s == 'Male':
        
            males.append(1)
            
        else:
        
            males.append(0)
            
    return males
    
def removeFemales(Matrix, MatrixIndex):

    count = 0

    males = []
        
    for rows in Matrix:

    #This loop forms the matrix of only males using the malesIndex created in getMales

        if MatrixIndex[count] == 1:

            males.append(rows[:-1])
            
        count += 1

    for s in range(len(MatrixIndex)):

        if MatrixIndex[s] == 0:
    
            for r in range(len(males)):
        
                males[r][s+1] = 'x'
                #print s
            
    return males
    
def getFatherSonList(Matrix):

    fatherSonList = []
    fatherSon = []
    
    for rows in Matrix:

        for r in range(len(rows)-1):
        
            if rows[r+1] == '1':
            
                fatherSon.append(r+1)
                fatherSon.append(rows[0])
                fatherSonList.append(fatherSon)
                fatherSon = []
        
    return fatherSonList
                
'''
csv_path = '/Users/quero/Desktop/ML/SemesterProject/mid3.csv'

with open(csv_path, "rb") as f_obj:

    matrix = csv_reader(f_obj)
    
    malesIndex = getMales(matrix)
    
    matrix = matrix[1:]
    
count = 0

males = []
    
for rows in matrix:

#This loop forms the matrix of only males using the malesIndex created in getMales

    if malesIndex[count] == 1:

        males.append(rows[:-1])
        
    count += 1
    
count = 0

newMales = np.copy(males)
newMales = newMales.tolist()

newMales = removeFemales(newMales, malesIndex)
    
FatherSonList = getFatherSonList(newMales)

print FatherSonList

'''
