#!/bin/python3
''' The following script takes as input a directory and reads in all files within that directory and renames them in a convention for downstream analysis '''
''' Version: 2.0 '''
''' Date: August 17th, 2023 '''
''' Publisher: Travis Haight '''
import os
import argparse

def rename_files(directory):
    R1_list = []
    R2_list = []
    files_mod = []
    files_mod_2 = []
    R1_list_mod = []
    R2_list_mod = []
    #Save all files in the supplied directory
    files = os.listdir(directory)
    #Check if files have R1/R2 convention and change based off some common coventions
    #You can add different conventions to this search just ensure you follow the format
    for file in files:
        if 'r1' in file:
            new_name = file.replace('r1', 'R1')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files_mod.append(new_name)
        elif 'read1' in file:
            new_name = file.replace('read1', 'R1')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files_mod.append(new_name)
        elif 'data1' in file:
            new_name = file.replace('data1', 'R1')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files_mod.append(new_name)
        elif 'Data1' in file:
            new_name = file.replace('Data1', 'R1')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files_mod.append(new_name)
        elif 'r2' in file:
            new_name = file.replace('r2', 'R2')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files_mod.append(new_name)
        elif 'read2' in file:
            new_name = file.replace('read2', 'R2')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files_mod.append(new_name)
        elif 'data2' in file:
            new_name = file.replace('data2', 'R2')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files_mod.append(new_name)
        elif 'Data2' in file:
            new_name = file.replace('Data2', 'R2')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files_mod.append(new_name)
        else:
            files_mod.append(file)
            #Check convention of .fq and convert to .fastq if needed for downstream analysis
    for file in files_mod:
        if 'fq' in file:
            new_name = file.replace('fq', 'fastq')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files_mod_2.append(new_name)

    #Split files into seperate read lists
    for file in files_mod_2:
        if 'R1' in file:
            R1_list.append(file)
        elif 'R2' in file:
            R2_list.append(file)

    #Rename R1_list
    for file in R1_list:
        if file.endswith('.fastq.gz'):
            if not file.endswith('R1.fastq.gz'):
                new_name = file.split('R1')[0] + 'R1.fastq.gz'
                os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
                R1_list_mod.append(new_name)
            else:
                R1_list_mod.append(file)
        if file.endswith('.fastq'):
            if not file.endswith('R1.fastq'):
                new_name = file.split('R1')[0] + 'R1.fastq'
                os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
                R1_list_mod.append(new_name)
            else:
                R1_list_mod.append(file)

    #Rename R2_list
    for file in R2_list:
        if file.endswith('.fastq.gz'):
            if not file.endswith('R2.fastq.gz'):
                new_name = file.split('R2')[0] + 'R2.fastq.gz'
                os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
                R2_list_mod.append(new_name)
            else:
                R2_list_mod.append(file)
        if file.endswith('.fastq'):
            if not file.endswith('R2.fastq'):
                new_name = file.split('R2')[0] + 'R2.fastq'
                os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
                R2_list_mod.append(new_name)
            else:
                R2_list_mod.append(file)

    return R1_list_mod, R2_list_mod

#Usage
parser = argparse.ArgumentParser(description='Supply this script with the absolute path to a folder that contains all your sample files. It will rename the files in the proper convention for pipeline use.')
parser.add_argument('-i', '--input', help='Absolute path to project folder. Ensure that it does not end with "/" for example: /home/test/project1')
args = parser.parse_args()
project = args.input
list1, list2 = rename_files(project)
print("List 1:", list1)
print("List 2:", list2)


 
