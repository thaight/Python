#!/bin/python/3
import os
import re
import shutil
#Absolute path to the folder containing all the files
path = "/scratch/thaight/brain-bank-illumina/R1/"
#Absolute path to the folder where you want the base folders created
raw = "/scratch/thaight/brain-bank-illumina/"
#Creates a list of all samples in a given path
mylist = os.listdir(path)

for file in mylist:
    #Adjust this for whatever delimiters are present in your files, can add more and seperate via |
    temp = re.split('-|_',file)
    #Adjust this based on the number of splits but generally folders are named after start information
    outpath = raw + temp[0] + "_" + temp[1]
    #Check if the base folder exists
    exists = os.path.exists(outpath)
    if not exists:
        #Create base folder if it doesnt exist so that raw files can be moved into it
        rawpath = outpath + "/raw"
        os.makedirs(rawpath)
    sourcepath = path + file
    destinationpath = outpath + "/raw/" + file
    shutil.move(sourcepath, destinationpath)



