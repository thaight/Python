#!/bin/python3
'''
The following script serves the following functions:
1: Renames files so that they contain the proper formating for downstream use: Users can add more conventions but ensure that you follow syntax.
2: Checks if files are compressed (.gz) and uncompresses them for downstream use.
3: Sets up directory systems (/raw, /output, /scripts) for downstream use and moves files into the /raw subfolder: Users can add other folder systems but ensure that you follow syntax.
4: Creates gtf.list, and geneout.list for downstream use: Currently users still need to adjust the gtf.list to define what is treated vs control for DE identification
Version: 3.0
Date: August 24th, 2023
Publisher: Travis Haight
'''
'''
The following is WIP notes for future functions:
Set a mode for circ/linear since if it is linear you will not need to create the .gtf and .geneout files
'''
import os
import shutil
import argparse
import gzip

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

def uncompress_gz_file(directory, file):
    ''' This function takes as input a file that ends with .gz and uncompresses it for downstream analysis '''
    file_path = directory + "/" + file
    output_file_path = file_path[:-3]
    #Initially open the compressed file in binary mode
    with gzip.open(file_path, 'rb') as compress_file:
        with open(output_file_path, 'wb') as output_file:
            shutil.copyfileobj(compress_file, output_file)
    print(f"Uncompressed {file_path} to {output_file_path}")
    #Remove .gz file
    os.remove(file_path)
    print(f"Removed {file_path}")

def dir_setup(directory):
    ''' This function takes the input directory as input sets up the file system for the pipeline to run off, and returns the mode (PE or SE)'''
    ''' This function requires that all raw files are in the same starting directory '''
    #Check if files are compressed (.gz) and uncompress if needed
    prefix_list = []
    #Remove tailing back slash from path
    directory = directory.rstrip("/")
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
    if len(files) == 0:
        return()
    if mode == "SE":
        for file in files:
            #Grab the sample prefix to create the base folder, and sample list for downstream use
            prefix = os.path.splitext(file)[0]
            prefix_folder = os.path.join(directory, prefix)
            prefix_list.append(prefix)
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
            #Grab the sample prefix to create base folder, and sample list for downstream use
            prefix = file.replace("_R1.fastq", "").replace("_R2.fastq", "")
            prefix_folder = os.path.join(directory, prefix)
            prefix_list.append(prefix)
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
    return(prefix_list)

def list_maker(directory, prefix):
    ''' This function takes the input directory as input sets up the file system for the pipeline to run off, and returns the mode (PE or SE)'''
    ''' This function requires that all raw files are in the same starting directory '''
    #Remove tailing back slash from path
    directory = directory.rstrip("/")
    unique_list = list(set(prefix))
    project = directory.split("/")[-1]
    all_samples = project + ".list"
    all_gtf = project + "_gtf.list"
    all_geneout = project + "_geneout.list"
    sample_list = os.path.join(directory, all_samples)
    gtf_list = os.path.join(directory, all_gtf)
    geneout_list = os.path.join(directory, all_geneout)
    with open(sample_list, 'w') as samples, open(gtf_list, 'w') as gtf, open(geneout_list, 'w') as geneout:
        samples.write("sample_ID" + '\t')
        samples.write("condition" + '\t')
        samples.write("replicate" + '\n')
        for file in unique_list:
            samples.write(str(file) + '\t')
            samples.write("X" + '\t')
            samples.write("Y" + '\n')
            gtf.write(str(file) + '\t')
            gtfpath = gtfpath = directory + "/" + file + "/output/" + file + ".gtf"
            gtf.write(gtfpath + '\t')
            gtf.write("X" + '\n')
            geneout.write(str(file) + '\t')
            geneoutpath = directory + "/" + file + "/output/gene/" + file + "_out.gtf"
            geneout.write(geneoutpath + '\n')
        samples.close()
        gtf.close()
        geneout.close()

#Main usage starts here
parser = argparse.ArgumentParser(description='Pipeline for the setup of new projects')
parser.add_argument('-i', '--input', help='Full path to folder containing the raw files. Example usage: /home/test/project1/')
args = parser.parse_args()
input = args.input
rename_files(input)
prefix = dir_setup(input)
list_maker(input, prefix)
