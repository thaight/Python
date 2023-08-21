#!/bin/python3
''' The following script takes as input an in and out directory, in which the in directory contains files and the out directory is the folder to write out to. The purpose is to create blank files for testi>
''' Version: 2.0 '''
''' Date: August 18th, 2023 '''
''' Publisher: Travis Haight '''
import os
import shutil
import argparse
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
parser = argparse.ArgumentParser(description='Supply this script with the absolute path to a folder containing samples, and the absolute path to a folder you want to create for testing')
parser.add_argument('-i', '--input', help='Absolute path to a folder containing samples. Ensure that it does not end with "/" for example: /home/test/project1')
parse.add_argument('-o', '--output', help='Absolute path to the output folder, Ensure that it does not end with "/" for example: /home/test/project1. Note: It does not need to exist.')
args = parser.parse_args()
input_dir = args.input
output_dir = args.output
create_blank_files(input_dir, output_dir)



