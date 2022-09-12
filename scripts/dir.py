import os
import shutil
import glob
#Change myliseR1 and mylistR2 to match paths to files
mylistR1 = glob.glob("/scratch/thaight/AtoI_HT22/*R1*.fastq") #Returns all R1 paths
mylistR2 = glob.glob("/scratch/thaight/AtoI_HT22/*R2*.fastq") #Rreturns all R2 paths
for R1Path in mylistR1:
        x = os.path.basename(R1Path).split("_")[0] #Returns prefix for each sample file
        R1_source = R1Path
        R1_dir = "/scratch/thaight/AtoI_HT22/" + x + "/raw/"
        try:
            	os.makedirs(R1_dir)
        except OSError as error:
                print(error)
        shutil.move(R1_source, R1_dir)

for R2Path in mylistR2:
        x = os.path.basename(R2Path).split("_")[0] #Returns prefix for each sample file
        R2_source = R2Path
        R2_dir = "/scratch/thaight/AtoI_HT22/" + x + "/raw/"
        shutil.move(R2_source,R2_dir)




