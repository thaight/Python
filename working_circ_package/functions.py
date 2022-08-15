#!/bin/python/3

import os.path
import sys
import subprocess


#SRA_prefix_grabber take the imput list and returns seperate lists for control and treated for downstream DE anlysis
def sample_prefix_grabber(sample_list):
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

def SRA_download(sample_data,sample_type):
        if sample_type == "SRA":
                for X in sample_data:
                        rc = subprocess.call(["./SRA_download.sh", X])
                        #subprocess.call(["./SRA_download.sh",X])

        return()

#def slurm_submit()



sample_type = "SRA"
sample_data = sample_prefix_grabber("/home/thaight/projects/rrg-zovoilis/thaight/total_circRNA_pipeline_v1/temp.list")
SRA_download(sample_data,sample_type)
