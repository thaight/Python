## Collection of Python Scripts

This is a collection of python scripts with the usage outlined for each below: <br />

fastq_filtering.py <br />

python fastq_filtering.py -i inputfile -l readlength -o outputfile <br />

dir.py  #Need to currently change the paths to your files <br />

python dir.py <br />

-----------------------------------------------------------------------------------------------------------------------------------------------------------
Script: listmaker.py <br /> 

Use: Takes the absolute path as an argument and creates a list of all files within that subdirectory  <br />

Dependecies: Ensure that python3 is loaded or installed <br />

Arguments: <br />
-i Absolute path to the folder you are making a list of ensure doesnt end with / <br />
-p prefix <br />
-l Absolute path to list if user wants to define samples, by default searches for all <br />

 <br />
Example Usage: python listmaker.py -i /path -p sample -l /path/sample.list <br />
Note: Ensure that -i path does not end with a slash or else it breaks the pathing system <br />
Note: Ensure that -l list does not contain trailing whitespace in the list file <br />

-----------------------------------------------------------------------------------------------------------------------------------------------------------
Script: fastq_split.py <br />
 <br />
Use: Takes a fastq file as input as well as the desired length and splits the fastq file in X length <br />

Dependencies: Ensure that python3 is loaded of installed <br />

Arugments:
-o Absolute path to file you want the output to go to
-i Absolute path to the input file (Note: Must be fastq)
-p Prefix of output files
-n Length of created files by defult is 1,000,000 (Note: 4 lines per read, therefore if you want 1000 reads you will set -n as 4000)

Example Usage: python3 fastq_split.py -o /path/ -i input.fastq -p sample -n 4000

-----------------------------------------------------------------------------------------------------------------------------------------------------------


