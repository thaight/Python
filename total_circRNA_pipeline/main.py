#!/bin/python/3

import os.path
import sys
import subprocess
import os
import logging


def sample_prefix_grabber(sample_list):
    """ Use: Obtain list of sample prefixes for downstream use """
    #Check that the SRA_list path exists
    if os.path.exists(sample_list) == False:
        sys.exit("Please review the manual")
    else:
        #Open SRA_list file to obtain the SRA prefix for download
        with open(sample_list, 'r') as sample_file:
            sample_data = []
            for line in sample_file:
                content_check = line.rstrip().split()
                sample_data.append(content_check[0])
            #Returns the sample prefix as an array
            return(sample_data)

def SRA_download(sample_data,sample_type,SRApath):
    """ Use: Download SRA files """
    if sample_type == "SRA":
        script_dir = SRApath + "SRA-download_"
        for X in sample_data:
            command = script_dir + X + ".sh"
            subprocess.run([command, X, SRApath])
    else:
        print ("No Files to Download")
        return()

def prepend_line(line, prefix, version, path):
    """ Use: Insert a given line to the top of a file for submission to slurm schedulers """
    # Define name of temporary dummy file for every prefix
    for ID in prefix:
        file_name = path + "SRA-download" #NEED TO FIX THIS SO THAT YOU PARSE A VARIAB>
        temp_file = file_name + "_" + ID + ".sh"
        # Open original file in read mode and temp file in write mode
        with open(file_name, 'r') as read_obj, open(temp_file, 'w') as write_obj:
            # Write shebang line to temp file
            write_obj.write("#!/bin/bash" + '\n')
            write_obj.write("#SBATCH --job-name=" + ID + "_SRA_download" + '\n')
            for X in line:
                # Write run time parameteres for each element of line
                write_obj.write("#SBATCH " + X + '\n')
            # Write in module load information needed
            write_obj.write("#module load " + version + '\n')
            # Read lines from original file one by one and append them to the temp file
            for obj in read_obj:
                write_obj.write(obj)
            # Makes the new scripts executable
            make_executable(temp_file)

def make_executable(path):
    """ Use: Takes a script as input and makes it executable """
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)

def directory_setup(prefix,path):
    """ Use: Takes a path and prefix and creates a directory if it doesnt exist """
    for item in prefix:
       dir = path + "/" + item + "/raw"
       if not os.path.isdir(dir):
          os.makedirs(dir)
       dir = path + "/" + item + "/scripts"
       if not os.path.isdir(dir):
           os.makedirs(dir)





#Need to assign these
SRA_mem  = "--mem=24G"
SRA_time = "--time=24:00:00"
account = "--account=rrg-zovoilis"
SRA_run_config = (SRA_time,SRA_mem,account)

#Need to either assign these from a config file or user needs to edit here
SRA_toolkit = "StdEnv/2022 gcc/9.3.0 sra-toolkit/3.0.0"
data_type = "SRA"
SRApath = "/home/travis/Desktop/Spyder3/"
SRA_list = SRApath + "temp.list"

SRA_prefix = sample_prefix_grabber(SRA_list) #Returns array of sample prefix

prepend_line(SRA_run_config,SRA_prefix,SRA_toolkit,SRApath) #Creates a SRA-download script for every sample prefix

directory_setup(SRA_prefix,SRApath) #Sets up directories

SRA_download(SRA_prefix, data_type, SRApath) #Submites the various SRA-download scripts to download files



