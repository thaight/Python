This is a work in progress that will allow for the full automation in the detection of circRNA as well as DE annotation, slice site annotation and downstream editing annotation



This package is optimized to currently work on cedar for the zovoilis lab

Edit temp.list to include a list of your sample prefixes


initially run module load python/3.10

then you can use the package as follows


python main.py -p /home/thaight/projects/rrg-zovoilis/thaight/circular_RNA_detection/CIRIquant/ -o /scratch/thaight/test_pipeline/ -l /home/thaight/projects/rrg-zovoilis/thaight/circular_RNA_detection/CIRIquant/temp.list -m USER


-p is the absolute path to the script folder
-o is the absolute path to the output folder
-l is the absolute path to the file list
-m Currently accepts USER for user supplied data or SRA for data to be downloaded from SRA
