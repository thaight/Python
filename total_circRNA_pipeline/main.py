#!/bin/python/3

import os.path
import sys
import subprocess
import os
import argparse


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

def SRA_download(sample_data,INpath,OUTpath):
    """ Use: Download SRA files """
    script_dir = INpath + "SRA-download_"
    for X in sample_data:
        command = script_dir + X + ".sh"
        subprocess.run([command, X, INpath, OUTpath])
    return()

def prepend_line(line, prefix, version, path, use):
    """ Use: Insert a given line to the top of a file for submission to slurm schedulers """
    for ID in prefix: # Define name of temporary dummy file for every prefix
        file_name = path
        temp_file = file_name + "_" + ID + ".sh"
        with open(file_name, 'r') as read_obj, open(temp_file, 'w') as write_obj: # Open original file in read mode and temp file in write mode
            write_obj.write("#!/bin/bash" + '\n') # Write shebang line to temp file
            write_obj.write("#SBATCH --job-name=" + ID + use + '\n')
            for X in line:
                write_obj.write("#SBATCH " + X + '\n') # Write run time parameteres for each element of line
            for Y in version:
                write_obj.write("#module load " + Y + '\n') # Write in module load information needed         
            for obj in read_obj: # Read lines from original file one by one and append them to the temp file
                write_obj.write(obj)
            make_executable(temp_file) # Makes the new scripts executable

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

def combine_name_version(config):
    with open(config, 'r') as config_file:
        software_name = []
        software_version = []
        software = []
        count = 0
        for line in config_file:
            content_check = line.rstrip().split()
            software_name.append(content_check[0])
            software_version.append(content_check[1])
        for item in software_name:
            X = software_name[count] + "/" + software_version[count]
            software.append(X)
            count = count + 1
        return(software)

def CIRI_quant(sample_data,INpath,OUTpath,config,pipepath):
    """ Use: Run pipeline on files """
    script_dir = INpath + "init_CIRIquant.sh"
    for X in sample_data:
        read1 = OUTpath + X + "/raw/" + X + "_R1.fastq"
        read2 = OUTpath + X + "/raw/" + X + "_R2.fastq"
        subprocess.run([script_dir, X, read1, read2, OUTpath, config])
    return()


parser = argparse.ArgumentParser(description='Analyze Sequencing Data for circRNA analysis.')
parser.add_argument("-p", "--pipeline", help="Absolute path to pipeline folder.")
parser.add_argument("-o", "--output", help="Absolute path to output folder.")
parser.add_argument("-l", "--list", help="Absolute path to file list.")
parser.add_argument("-m", "--mode", help="Current accepted modes are SRA or USER.")
args = parser.parse_args()
pipelinepath = args.pipeline
OUTpath = args.output
sample_list = args.list
data_type = args.mode

#Need to assign these
SRA_mem  = "--mem=24G" #Need to find a way to better estimate SRA download speeds
SRA_time = "--time=24:00:00" #Need to fine a way to better estimate SRA download times

CIRI_mem = "--mem=8G" #Need to change this so it is based off read count measure
CIRI_time = "--time=12:00:00" #Need to change this so it is based off read count measure

account = "--account=rrg-zovoilis" #User Defined
SRA_run_config = (SRA_time,SRA_mem,account) #Default SRA memory and time reqs
CIRI_run_config = (CIRI_time,CIRI_mem,account)

cedar_config = pipelinepath + "cedar.config"
CIRI_config = pipelinepath + "CIRI.yaml"

software = combine_name_version(cedar_config) #Obtains software version information from config.list
StdEnv = software[0]
gcc = software[1]
sra_toolkit = software[2]
bwa = software[3]
hisat2 = software[4]
samtools = software[5]
stringtie = software[6]
biocond = software[7]

SRA_software = (StdEnv,gcc,sra_toolkit) #Software needed for SRA-toolkit
CIRI_software = (bwa,hisat2,samtools,stringtie)
sample_prefix = sample_prefix_grabber(sample_list) #Returns array of sample prefix

directory_setup(sample_prefix,OUTpath) #Sets up directories
if data_type == "SRA":
    SRApath = pipelinepath + "SRA-download"
    prepend_line(SRA_run_config,sample_prefix,SRA_software,SRApath,"_SRA_download") #Creates a SRA-download script for every sample prefix
    SRA_download(sample_prefix, pipelinepath, OUTpath) #Submites the various SRA-download scripts to download files
elif data_type == "USER":
    print ("No Data to Download from SRA, starting pipeline.")
CIRIpath = pipelinepath + "run_CIRIquant"
prepend_line(CIRI_run_config,sample_prefix,CIRI_software,CIRIpath,"_CIRIquant")
CIRI_quant(sample_prefix,pipelinepath,OUTpath,CIRI_config,pipelinepath)
