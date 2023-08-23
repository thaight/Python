#!/bin/python3
''' The following script takes as input a directory and first checks if files are .gz compressed and uncompresses them if needed before setting the project directory up for future use '''
''' Currently only sets up /raw /output /scripts but that can be adjusted if users want other folder systems '''
''' Version: 1.0 '''
''' Date: August 18th, 2023 '''
''' Publisher: Travis Haight '''
import os
import shutil
import argparse
import gzip

def uncompress_gz_file(directory, file):
    ''' This function takes as input a file that ends with .gz and uncompresses it for downstream analysis '''
    file_path = directory + file
     #Initially open the compressed file in binary mode
    with gzip.open(file_path, 'rb') as compress_file:
        #Read through the compressed file
        compressed_data = compress_file.read()
    #Remove .gz from file format for downstream analysis
    output_file_path = file_path[:-3]
    #Write out the uncompressed file contents
    with open(output_file_path, 'wb') as output_file:
        output_file.write(compressed_data)
    print(f"Uncompressed {file_path} to {output_file_path}")
    #Remove .gz file
    os.remove(file_path)
    print(f"Removed {file_path}")

def dir_setup(directory):
    ''' This function takes the input directory as input sets up the file system for the pipeline to run off, and returns the mode (PE or SE)'''
    ''' This function requires that all raw files are in the same starting directory '''
    #Check if files are compressed (.gz) and uncompress if needed
    files_gz = [file for file in os.listdir(directory) if file.endswith(".gz")]
    for file in files_gz:
        uncompress_gz_file(directory, file)
    files = [file for file in os.listdir(directory) if file.endswith(".fastq")]
    #Set the mode based off samples
    for file in files:
        if "R2" in file or "R1" in file:
            mode = "PE"
        else:
            mode = "SE"
    if mode == "SE":
      for file in files:
            #Grab the sample prefix to create the base folder
            prefix = os.path.splitext(file)[0]
            prefix_folder = os.path.join(directory, prefix)
            if not os.path.exists(prefix_folder):
                os.makedirs(prefix_folder)
                print(f"Folder '{prefix_folder}' created successfully.")
            #Create subfolders inside the prefix base folder
            raw_folder = os.path.join(prefix_folder, "raw")
            output_folder = os.path.join(prefix_folder, "output")
            scripts_folder = os.path.join(prefix_folder, "scripts")
            if not os.path.exists(raw_folder):
                os.makedirs(raw_folder)
                print(f"Folder '{raw_folder}' created successfully.")
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
                print(f"Folder '{output_folder}' created successfully.")
            if not os.path.exists(scripts_folder):
                os.makedirs(scripts_folder)
                print(f"Folder '{scripts_folder}' created successfully.")
            #Move the raw fastq files into the prefix/raw folder for downstream use
            file_path = os.path.join(directory, file)
            new_file_path = os.path.join(raw_folder, file)
            shutil.move(file_path, new_file_path)
            print(f"File '{file}' moved to the 'raw' subfolder of '{prefix}'.")

    elif mode == "PE":
        for file in files:
            print(file)
            #Grab the sample prefix to create base folder
            prefix = file.replace("_R1.fastq", "").replace("_R2.fastq", "")
            prefix_folder = os.path.join(directory, prefix)
            if not os.path.exists(prefix_folder):
                os.makedirs(prefix_folder)
                print(f"Folder '{prefix_folder}' created successfully.")
            #Create subfolders inside the prefix base folder
            raw_folder = os.path.join(prefix_folder, "raw")
            output_folder = os.path.join(prefix_folder, "output")
            scripts_folder = os.path.join(prefix_folder, "scripts")
            if not os.path.exists(raw_folder):
                os.makedirs(raw_folder)
                print(f"Folder '{raw_folder}' created successfully.")
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
                print(f"Folder '{output_folder}' created successfully.")
            if not os.path.exists(scripts_folder):
                os.makedirs(scripts_folder)
                print(f"Folder '{scripts_folder}' created successfully.")
            #Move the raw fastq files into the prefix/raw folder for downstream use
            file_path = os.path.join(directory, file)
            new_file_path = os.path.join(raw_folder, file)
            shutil.move(file_path, new_file_path)
            print(f"File '{file}' moved to the 'raw' subfolder of '{prefix_folder}'.")
    return(mode)

#Main pipeline starts here
parser = argparse.ArgumentParser(description='Pipeline for the detection and quantification of circRNA expression.')
parser.add_argument('-i', '--input', help='Full path to folder containing the raw files')
args = parser.parse_args()
input = args.input
mode = dir_setup(input)



