#!/bin/python3
''' The following script takes as input an in and out directory, in which the in directory contains files and the out directory is the folder to write out to. The purpose is to create blank files for testi>
''' Version: 1.0 '''
''' Date: August 18th, 2023 '''
''' Publisher: Travis Haight '''
import os
import shutil

def create_blank_files(input_directory, output_directory):
    #Get list of files
    file_names = os.listdir(input_directory)
    #Check output directory and create if it doesnt exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    #Loop through each file name and create a blank file in the output directory
    for file_name in file_names:
        #Create the full path of the output file
        output_file_path = os.path.join(output_directory, file_name)
        #Create a blank file in the output directory
        with open(output_file_path, 'w') as f:
            pass
        print(f"Created file: {output_file_path}")

#Usage
input_directory = '/home/thaight/projects/rrg-zovoilis/thaight/projects/calgary_brain_bank'
output_directory = '/home/thaight/projects/rrg-zovoilis/thaight/projects/project_test'
create_blank_files(input_directory, output_directory)
