#!/bin/python3
''' The following script takes as input a directory and reads in all files within that directory and renames them in a convention for downstream analysis '''
''' Version: 1.0 '''
''' Date: August 17th, 2023 '''
''' Publisher: Travis Haight '''
import os

def rename_files(directory):
    R1_list = []
    R2_list = []
    #Save all files in the supplied directory
    files = os.listdir(directory)

    #Check if files have R1/R2 convention and change based off some common coventions
    #You can add different conventions to this search just ensure you follow the format
    for file in files:
        if 'r1' in file:
            new_name = file.replace('r1', 'R1')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files.remove(file)
            files.append(new_name)
        elif 'read1' in file:
            new_name = file.replace('read1', 'R1')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files.remove(file)
            files.append(new_name)
        elif 'r2' in file:
            new_name = file.replace('r2', 'R2')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files.remove(file)
            files.append(new_name)
        elif 'read2' in file:
            new_name = file.replace('read2', 'R2')
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            files.remove(file)
            files.append(new_name)

    #Split files into seperate read lists
    for file in files:
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
                R1_list.remove(file)
                R1_list.append(new_name)
        if file.endswith('.fastq'):
            if not file.endswith('R1.fastq'):
                new_name = file.split('R1')[0] + 'R1.fastq'
                os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
                R1_list.remove(file)
                R1_list.append(new_name)

    #Rename R2_list
    for file in R2_list:
        if file.endswith('fastq.gz'):
            if not file.endswith('R2.fastq.gz'):
                new_name = file.split('R2')[0] + 'R2.fastq.gz'
                os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
                R2_list.remove(file)
                R2_list.append(new_name)
        if file.endswith('.fastq'):
            if not file.endswith('R2.fastq'):
                new_name = file.split('R2')[0] + 'R2.fastq'
                os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
                R2_list.remove(file)
                R2_list.append(new_name)

    return R1_list, R2_list



#Usage
#Current need to change directory, future versions should allow for variable parsing
directory = '/home/thaight/projects/rrg-zovoilis/thaight/projects/test2'
list1, list2 = rename_files(directory)
print("List 1:", list1)
print("List 2:", list2)
