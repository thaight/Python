#!/bin/python3
''' The following script takes as input a directory and a string. It then removes the string from each file within that directory '''
''' Version: 1.0 '''
''' Date: August 23th, 2023 '''
''' Publisher: Travis Haight '''
import os
import argparse

def remove_string_from_filenames(directory, string):
    #Save all the files in the supplied directory
    files = os.listdir(directory)
    for file in files:
        #Check for string
        if string in file:
            #Create new file name
            new_name = file.replace(string, "")
            #Rename the file
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            print(f"Renamed {file} to {new_name}")

#Main Usage
parser = argparse.ArgumentParser(description='Pipeline for the detection and quantification of circRNA expression.')
parser.add_argument('-i', '--input', help='Absolute path to project folder. Ensure that it does not end with "/" for example: /home/test/project1')
parser.add_argument('-s', '--string', help='String to remove from file names')
args = parser.parse_args()
input = args.input
string = args.string
remove_string_from_filenames(input, string)
