## Collection of Python Scripts

This is a collection of python scripts with the usage outlined for each below:

fastq_filtering.py

python fastq_filtering.py -i inputfile -l readlength -o outputfile

dir.py  #Need to currently change the paths to your files

python dir.py

-----------------------------------------------------------------------------------------------------------------------------------------------------------
Script: listmaker.py

Use: Takes the absolute path as an argument and creates a list of all files within that subdirectory

Dependecies: Ensure that python3 is loaded or installed

Arguments:
-i Absolute path to the folder you are making a list of ensure doesnt end with /
-p prefix


Example Usage: python listmaker.py -i /path/ -p sample

-----------------------------------------------------------------------------------------------------------------------------------------------------------
Script: fastq_split.py

Use: Takes a fastq file as input as well as the desired length and splits the fastq file in X length

Dependencies: Ensure that python3 is loaded of installed

Arugments:
-o Absolute path to file you want the output to go to
-i Absolute path to the input file (Note: Must be fastq)
-p Prefix of output files
-n Length of created files by defult is 1,000,000 (Note: 4 lines per read, therefore if you want 1000 reads you will set -n as 4000)

Example Usage: python3 fastq_split.py -o /path/ -i input.fastq -p sample -n 4000

-----------------------------------------------------------------------------------------------------------------------------------------------------------


