import cv2 as cv
import os

def load_images_from_folder(folder):

    images = []
    for filename in os.listdir(folder):
        img = cv.imread(os.path.join(folder,filename))
        if img is not None:
            #print("image!")
            images.append(img)
    return images
    

def folderFind(rootdir, index, subindex):

    images = []

    for dirs in os.listdir(rootdir):
    
        if index == 0:
        
            subdirs = os.path.join(rootdir, dirs)
            
            images = load_images_from_folder(subdirs + "/MID" + str(subindex))
            
        index = index - 1
        
    return images
    
def getCSV(rootdir, index):

    for dirs in os.listdir(rootdir):
    
        if index == 0:
        
            csv = open(rootdir + '/' + dirs + '/mid.csv', 'rb')
            
            #print dirs
            
        index = index - 1
        
    return csv
        
rootdir = '/Users/quero/Desktop/ML/SemesterProject/FIDs_NEW'


#print csv
#print data
#print(images)
